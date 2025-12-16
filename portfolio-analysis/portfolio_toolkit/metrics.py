"""Financial performance metrics and calculations.

This module provides functions for calculating portfolio returns, volatility,
risk-adjusted metrics, and performance statistics.
"""

import pandas as pd
import numpy as np
from typing import Dict, Optional, Union


def calculate_returns(
    prices: Union[pd.Series, pd.DataFrame],
    method: str = 'simple',
    periods: int = 1
) -> Union[pd.Series, pd.DataFrame]:
    """Calculate returns from price data.
    
    Parameters
    ----------
    prices : pd.Series or pd.DataFrame
        Price time series or DataFrame
    method : str, default 'simple'
        Return calculation method ('simple' or 'log')
    periods : int, default 1
        Number of periods for return calculation
        
    Returns
    -------
    pd.Series or pd.DataFrame
        Calculated returns
        
    Examples
    --------
    >>> returns = calculate_returns(prices, method='simple')
    >>> log_returns = calculate_returns(prices, method='log')
    """
    if method == 'simple':
        returns = prices.pct_change(periods=periods)
    elif method == 'log':
        returns = np.log(prices / prices.shift(periods))
    else:
        raise ValueError(f"Unknown method: {method}. Use 'simple' or 'log'")
    
    return returns


def calculate_cumulative_returns(returns: pd.Series) -> pd.Series:
    """Calculate cumulative returns from periodic returns.
    
    Parameters
    ----------
    returns : pd.Series
        Periodic returns
        
    Returns
    -------
    pd.Series
        Cumulative returns (starts at 0)
    """
    return (1 + returns).cumprod() - 1


def calculate_cagr(
    prices: pd.Series,
    periods_per_year: int = 252
) -> float:
    """Calculate Compound Annual Growth Rate (CAGR).
    
    Parameters
    ----------
    prices : pd.Series
        Price time series
    periods_per_year : int, default 252
        Trading days per year (252 for daily, 12 for monthly)
        
    Returns
    -------
    float
        CAGR as decimal (0.10 = 10%)
        
    Examples
    --------
    >>> cagr = calculate_cagr(prices)
    >>> print(f"CAGR: {cagr:.2%}")
    """
    total_return = prices.iloc[-1] / prices.iloc[0] - 1
    n_periods = len(prices) - 1
    years = n_periods / periods_per_year
    
    cagr = (1 + total_return) ** (1 / years) - 1
    return cagr


def calculate_volatility(
    returns: pd.Series,
    periods_per_year: int = 252,
    annualize: bool = True
) -> float:
    """Calculate volatility (standard deviation of returns).
    
    Parameters
    ----------
    returns : pd.Series
        Returns time series
    periods_per_year : int, default 252
        Periods per year for annualization
    annualize : bool, default True
        Whether to annualize volatility
        
    Returns
    -------
    float
        Volatility as decimal
    """
    vol = returns.std()
    
    if annualize:
        vol = vol * np.sqrt(periods_per_year)
    
    return vol


def calculate_sharpe_ratio(
    returns: pd.Series,
    risk_free_rate: float = 0.02,
    periods_per_year: int = 252
) -> float:
    """Calculate annualized Sharpe ratio.
    
    Parameters
    ----------
    returns : pd.Series
        Returns time series
    risk_free_rate : float, default 0.02
        Annual risk-free rate as decimal (0.02 = 2%)
    periods_per_year : int, default 252
        Periods per year (252 for daily, 12 for monthly)
        
    Returns
    -------
    float
        Sharpe ratio
        
    Examples
    --------
    >>> sharpe = calculate_sharpe_ratio(returns, risk_free_rate=0.02)
    >>> print(f"Sharpe Ratio: {sharpe:.2f}")
    """
    excess_returns = returns - risk_free_rate / periods_per_year
    return np.sqrt(periods_per_year) * excess_returns.mean() / returns.std()


def calculate_sortino_ratio(
    returns: pd.Series,
    risk_free_rate: float = 0.02,
    periods_per_year: int = 252
) -> float:
    """Calculate annualized Sortino ratio (downside deviation).
    
    Parameters
    ----------
    returns : pd.Series
        Returns time series
    risk_free_rate : float, default 0.02
        Annual risk-free rate as decimal
    periods_per_year : int, default 252
        Periods per year
        
    Returns
    -------
    float
        Sortino ratio
    """
    excess_returns = returns - risk_free_rate / periods_per_year
    downside_returns = returns[returns < 0]
    downside_std = downside_returns.std()
    
    if downside_std == 0:
        return np.inf
    
    return np.sqrt(periods_per_year) * excess_returns.mean() / downside_std


def calculate_calmar_ratio(
    returns: pd.Series,
    periods_per_year: int = 252
) -> float:
    """Calculate Calmar ratio (CAGR / Max Drawdown).
    
    Parameters
    ----------
    returns : pd.Series
        Returns time series
    periods_per_year : int, default 252
        Periods per year
        
    Returns
    -------
    float
        Calmar ratio
    """
    prices = (1 + returns).cumprod()
    cagr = calculate_cagr(prices, periods_per_year)
    max_dd_info = calculate_max_drawdown(prices)
    max_dd = abs(max_dd_info['max_drawdown'])
    
    if max_dd == 0:
        return np.inf
    
    return cagr / max_dd


def calculate_max_drawdown(prices: pd.Series) -> Dict[str, float]:
    """Calculate maximum drawdown and related metrics.
    
    Parameters
    ----------
    prices : pd.Series
        Price time series
        
    Returns
    -------
    dict
        Dictionary containing:
        - max_drawdown: Maximum drawdown as decimal
        - peak: Peak price before max drawdown
        - trough: Trough price at max drawdown
        - recovery: Days to recovery (or None if not recovered)
        
    Examples
    --------
    >>> mdd_info = calculate_max_drawdown(prices)
    >>> print(f"Max Drawdown: {mdd_info['max_drawdown']:.2%}")
    """
    cumulative = prices / prices.iloc[0]
    running_max = cumulative.cummax()
    drawdown = (cumulative - running_max) / running_max
    
    max_dd = drawdown.min()
    max_dd_idx = drawdown.idxmin()
    
    # Find peak before max drawdown
    peak_idx = running_max[:max_dd_idx].idxmax()
    peak = prices[peak_idx]
    trough = prices[max_dd_idx]
    
    # Find recovery (if any)
    recovery_idx = None
    recovery_days = None
    
    if max_dd_idx < len(prices) - 1:
        future_prices = prices[max_dd_idx:]
        recovered = future_prices[future_prices >= peak]
        if len(recovered) > 0:
            recovery_idx = recovered.index[0]
            recovery_days = (recovery_idx - max_dd_idx).days if hasattr(
                recovery_idx - max_dd_idx, 'days'
            ) else int(recovery_idx - max_dd_idx)
    
    return {
        'max_drawdown': max_dd,
        'peak': peak,
        'trough': trough,
        'peak_date': peak_idx,
        'trough_date': max_dd_idx,
        'recovery_date': recovery_idx,
        'recovery_days': recovery_days
    }


def calculate_alpha_beta(
    portfolio_returns: pd.Series,
    benchmark_returns: pd.Series,
    risk_free_rate: float = 0.02,
    periods_per_year: int = 252
) -> Dict[str, float]:
    """Calculate alpha and beta vs benchmark.
    
    Parameters
    ----------
    portfolio_returns : pd.Series
        Portfolio returns
    benchmark_returns : pd.Series
        Benchmark returns
    risk_free_rate : float, default 0.02
        Annual risk-free rate
    periods_per_year : int, default 252
        Periods per year
        
    Returns
    -------
    dict
        Dictionary with 'alpha' and 'beta'
    """
    # Align series
    aligned = pd.DataFrame({
        'portfolio': portfolio_returns,
        'benchmark': benchmark_returns
    }).dropna()
    
    # Calculate beta
    covariance = aligned['portfolio'].cov(aligned['benchmark'])
    benchmark_variance = aligned['benchmark'].var()
    beta = covariance / benchmark_variance
    
    # Calculate alpha (annualized)
    portfolio_mean = aligned['portfolio'].mean() * periods_per_year
    benchmark_mean = aligned['benchmark'].mean() * periods_per_year
    alpha = portfolio_mean - (risk_free_rate + beta * (benchmark_mean - risk_free_rate))
    
    return {
        'alpha': alpha,
        'beta': beta
    }


def calculate_information_ratio(
    portfolio_returns: pd.Series,
    benchmark_returns: pd.Series
) -> float:
    """Calculate information ratio (active return / tracking error).
    
    Parameters
    ----------
    portfolio_returns : pd.Series
        Portfolio returns
    benchmark_returns : pd.Series
        Benchmark returns
        
    Returns
    -------
    float
        Information ratio
    """
    active_returns = portfolio_returns - benchmark_returns
    tracking_error = active_returns.std()
    
    if tracking_error == 0:
        return np.inf
    
    return active_returns.mean() / tracking_error


def calculate_rolling_metric(
    returns: pd.Series,
    metric_func: callable,
    window: int = 252,
    **kwargs
) -> pd.Series:
    """Calculate rolling metric over time.
    
    Parameters
    ----------
    returns : pd.Series
        Returns time series
    metric_func : callable
        Function to calculate metric (e.g., calculate_sharpe_ratio)
    window : int, default 252
        Rolling window size
    **kwargs : dict
        Additional arguments for metric_func
        
    Returns
    -------
    pd.Series
        Rolling metric values
        
    Examples
    --------
    >>> rolling_sharpe = calculate_rolling_metric(
    ...     returns,
    ...     calculate_sharpe_ratio,
    ...     window=252,
    ...     risk_free_rate=0.02
    ... )
    """
    return returns.rolling(window).apply(
        lambda x: metric_func(x, **kwargs),
        raw=False
    )


def calculate_portfolio_statistics(
    returns: pd.Series,
    periods_per_year: int = 252
) -> Dict[str, float]:
    """Calculate comprehensive portfolio statistics.
    
    Parameters
    ----------
    returns : pd.Series
        Returns time series
    periods_per_year : int, default 252
        Periods per year
        
    Returns
    -------
    dict
        Dictionary of portfolio statistics
    """
    prices = (1 + returns).cumprod()
    
    stats = {
        'total_return': prices.iloc[-1] - 1,
        'cagr': calculate_cagr(prices, periods_per_year),
        'volatility': calculate_volatility(returns, periods_per_year),
        'sharpe_ratio': calculate_sharpe_ratio(returns, periods_per_year=periods_per_year),
        'sortino_ratio': calculate_sortino_ratio(returns, periods_per_year=periods_per_year),
        'calmar_ratio': calculate_calmar_ratio(returns, periods_per_year),
        'max_drawdown': calculate_max_drawdown(prices)['max_drawdown'],
        'mean_return': returns.mean() * periods_per_year,
        'median_return': returns.median() * periods_per_year,
        'skewness': returns.skew(),
        'kurtosis': returns.kurtosis(),
        'positive_periods': (returns > 0).sum() / len(returns),
        'negative_periods': (returns < 0).sum() / len(returns)
    }
    
    return stats
