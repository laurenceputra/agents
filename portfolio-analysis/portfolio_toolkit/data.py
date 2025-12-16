"""Portfolio data loading and cleaning utilities.

This module provides functions for loading portfolio data from various sources,
validating data quality, and preparing DataFrames for analysis.
"""

import pandas as pd
import numpy as np
from typing import Optional, List, Dict, Union
from pathlib import Path
import warnings


def load_portfolio_csv(
    filepath: Union[str, Path],
    date_column: str = 'date',
    symbol_column: str = 'symbol',
    shares_column: str = 'shares',
    price_column: str = 'price',
    parse_dates: bool = True
) -> pd.DataFrame:
    """Load portfolio data from CSV file with standardized column names.
    
    Parameters
    ----------
    filepath : str or Path
        Path to CSV file containing portfolio data
    date_column : str, default 'date'
        Name of column containing dates
    symbol_column : str, default 'symbol'
        Name of column containing ticker symbols
    shares_column : str, default 'shares'
        Name of column containing number of shares
    price_column : str, default 'price'
        Name of column containing prices
    parse_dates : bool, default True
        Whether to parse date column as datetime
        
    Returns
    -------
    pd.DataFrame
        Portfolio data with standardized columns
        
    Examples
    --------
    >>> df = load_portfolio_csv('portfolio.csv')
    >>> print(df.columns)
    Index(['date', 'symbol', 'shares', 'price', 'value'])
    """
    df = pd.read_csv(filepath, parse_dates=[date_column] if parse_dates else None)
    
    # Standardize column names
    column_mapping = {
        date_column: 'date',
        symbol_column: 'symbol',
        shares_column: 'shares',
        price_column: 'price'
    }
    df = df.rename(columns=column_mapping)
    
    # Calculate position value if not present
    if 'value' not in df.columns:
        df['value'] = df['shares'] * df['price']
    
    return df


def load_portfolio_excel(
    filepath: Union[str, Path],
    sheet_name: Union[str, int] = 0,
    **kwargs
) -> pd.DataFrame:
    """Load portfolio data from Excel file.
    
    Parameters
    ----------
    filepath : str or Path
        Path to Excel file
    sheet_name : str or int, default 0
        Sheet name or index to load
    **kwargs : dict
        Additional arguments passed to load_portfolio_csv
        
    Returns
    -------
    pd.DataFrame
        Portfolio data with standardized columns
    """
    df = pd.read_excel(filepath, sheet_name=sheet_name)
    
    # Save to temp CSV and use load_portfolio_csv for consistency
    temp_path = Path(filepath).parent / '.temp_portfolio.csv'
    df.to_csv(temp_path, index=False)
    result = load_portfolio_csv(temp_path, **kwargs)
    temp_path.unlink()  # Delete temp file
    
    return result


def fetch_price_history(
    symbols: Union[str, List[str]],
    start_date: str,
    end_date: str,
    source: str = 'yahoo',
    interval: str = '1d'
) -> pd.DataFrame:
    """Fetch historical price data from financial APIs.
    
    Parameters
    ----------
    symbols : str or list of str
        Ticker symbol(s) to fetch
    start_date : str
        Start date in YYYY-MM-DD format
    end_date : str
        End date in YYYY-MM-DD format
    source : str, default 'yahoo'
        Data source ('yahoo' or 'alphavantage')
    interval : str, default '1d'
        Data frequency ('1d', '1wk', '1mo')
        
    Returns
    -------
    pd.DataFrame
        Price history with DatetimeIndex and symbol columns
        
    Examples
    --------
    >>> prices = fetch_price_history(['AAPL', 'MSFT'], '2023-01-01', '2024-01-01')
    >>> print(prices.head())
                   AAPL    MSFT
    2023-01-03  125.07  239.58
    2023-01-04  126.36  231.92
    """
    if isinstance(symbols, str):
        symbols = [symbols]
    
    if source == 'yahoo':
        try:
            import yfinance as yf
            data = yf.download(
                symbols,
                start=start_date,
                end=end_date,
                interval=interval,
                progress=False
            )
            
            # Extract adjusted close prices
            if len(symbols) == 1:
                prices = data['Adj Close'].to_frame(name=symbols[0])
            else:
                prices = data['Adj Close']
            
            return prices
            
        except ImportError:
            raise ImportError(
                "yfinance not installed. Install with: pip install yfinance"
            )
    
    elif source == 'alphavantage':
        raise NotImplementedError(
            "Alpha Vantage support not yet implemented. Use source='yahoo'"
        )
    
    else:
        raise ValueError(f"Unknown source: {source}. Use 'yahoo' or 'alphavantage'")


def clean_portfolio_data(
    df: pd.DataFrame,
    drop_missing: bool = False,
    fill_method: Optional[str] = 'ffill'
) -> pd.DataFrame:
    """Clean and validate portfolio data.
    
    Parameters
    ----------
    df : pd.DataFrame
        Portfolio data to clean
    drop_missing : bool, default False
        Whether to drop rows with missing values
    fill_method : str or None, default 'ffill'
        Method to fill missing values ('ffill', 'bfill', None)
        
    Returns
    -------
    pd.DataFrame
        Cleaned portfolio data
        
    Raises
    ------
    ValueError
        If required columns are missing or data is invalid
    """
    required_columns = ['date', 'symbol', 'shares', 'price']
    missing_columns = set(required_columns) - set(df.columns)
    
    if missing_columns:
        raise ValueError(f"Missing required columns: {missing_columns}")
    
    # Check for invalid values
    if (df['shares'] < 0).any():
        warnings.warn("Negative share counts found. Converting to absolute values.")
        df['shares'] = df['shares'].abs()
    
    if (df['price'] <= 0).any():
        warnings.warn("Zero or negative prices found. These will be treated as missing.")
        df.loc[df['price'] <= 0, 'price'] = np.nan
    
    # Handle missing values
    if drop_missing:
        df = df.dropna()
    elif fill_method:
        df = df.fillna(method=fill_method) if fill_method in ['ffill', 'bfill'] else df
    
    # Sort by date
    df = df.sort_values('date').reset_index(drop=True)
    
    return df


def validate_portfolio_data(df: pd.DataFrame) -> Dict[str, Union[bool, List[str]]]:
    """Validate portfolio data quality and return report.
    
    Parameters
    ----------
    df : pd.DataFrame
        Portfolio data to validate
        
    Returns
    -------
    dict
        Validation report with status and issues found
        
    Examples
    --------
    >>> report = validate_portfolio_data(portfolio_df)
    >>> if report['valid']:
    ...     print("Data is valid!")
    >>> else:
    ...     print("Issues:", report['issues'])
    """
    issues = []
    
    # Check required columns
    required_columns = ['date', 'symbol', 'shares', 'price']
    missing_columns = set(required_columns) - set(df.columns)
    if missing_columns:
        issues.append(f"Missing columns: {missing_columns}")
    
    # Check for missing values
    missing_counts = df[required_columns].isnull().sum()
    if missing_counts.any():
        issues.append(f"Missing values: {missing_counts[missing_counts > 0].to_dict()}")
    
    # Check for duplicates
    if df.duplicated(subset=['date', 'symbol']).any():
        issues.append("Duplicate date-symbol combinations found")
    
    # Check date range
    if 'date' in df.columns:
        date_range = (df['date'].min(), df['date'].max())
        days = (date_range[1] - date_range[0]).days
        if days < 30:
            issues.append(f"Short date range: only {days} days")
    
    # Check for invalid symbols
    if 'symbol' in df.columns:
        invalid_symbols = df[df['symbol'].str.len() == 0]['symbol'].unique()
        if len(invalid_symbols) > 0:
            issues.append(f"Empty symbols found")
    
    return {
        'valid': len(issues) == 0,
        'issues': issues,
        'row_count': len(df),
        'symbols': df['symbol'].nunique() if 'symbol' in df.columns else 0,
        'date_range': (df['date'].min(), df['date'].max()) if 'date' in df.columns else None
    }


def merge_portfolio_with_prices(
    portfolio: pd.DataFrame,
    prices: pd.DataFrame,
    how: str = 'left'
) -> pd.DataFrame:
    """Merge portfolio holdings with historical price data.
    
    Parameters
    ----------
    portfolio : pd.DataFrame
        Portfolio holdings with columns: date, symbol, shares
    prices : pd.DataFrame
        Historical prices with DatetimeIndex and symbol columns
    how : str, default 'left'
        Type of merge ('left', 'inner', 'outer')
        
    Returns
    -------
    pd.DataFrame
        Merged portfolio with current prices
    """
    # Ensure portfolio date is datetime
    portfolio['date'] = pd.to_datetime(portfolio['date'])
    
    # Melt prices to long format
    prices_long = prices.reset_index().melt(
        id_vars=['Date'],
        var_name='symbol',
        value_name='current_price'
    )
    prices_long = prices_long.rename(columns={'Date': 'date'})
    
    # Merge
    merged = pd.merge(
        portfolio,
        prices_long,
        on=['date', 'symbol'],
        how=how
    )
    
    # Calculate current value
    merged['current_value'] = merged['shares'] * merged['current_price']
    
    return merged
