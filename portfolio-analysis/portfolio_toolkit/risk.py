"""Risk assessment and Value at Risk (VaR) calculations.

This module provides functions for portfolio risk analysis including VaR,
CVaR, stress testing, and Monte Carlo simulation.
"""

import pandas as pd
import numpy as np
from scipy import stats
from typing import Dict, Optional, Union, Tuple


def calculate_var(
    returns: pd.Series,
    confidence_level: float = 0.95,
    method: str = 'historical'
) -> float:
    """Calculate Value at Risk (VaR).
    
    Parameters
    ----------
    returns : pd.Series
        Returns time series
    confidence_level : float, default 0.95
        Confidence level (0.90, 0.95, 0.99)
    method : str, default 'historical'
        VaR calculation method ('historical', 'parametric', 'cornish-fisher')
        
    Returns
    -------
    float
        VaR as decimal (negative value indicates loss)
        
    Examples
    --------
    >>> var_95 = calculate_var(returns, confidence_level=0.95, method='historical')
    >>> print(f"95% VaR: {var_95:.2%}")
    """
    if method == 'historical':
        return returns.quantile(1 - confidence_level)
    
    elif method == 'parametric':
        mean = returns.mean()
        std = returns.std()
        z_score = stats.norm.ppf(1 - confidence_level)
        return mean + z_score * std
    
    elif method == 'cornish-fisher':
        mean = returns.mean()
        std = returns.std()
        skew = returns.skew()
        kurt = returns.kurtosis()
        
        z = stats.norm.ppf(1 - confidence_level)
        z_cf = (z +
                (z**2 - 1) * skew / 6 +
                (z**3 - 3*z) * kurt / 24 -
                (2*z**3 - 5*z) * skew**2 / 36)
        
        return mean + z_cf * std
    
    else:
        raise ValueError(
            f"Unknown method: {method}. Use 'historical', 'parametric', or 'cornish-fisher'"
        )


def calculate_cvar(
    returns: pd.Series,
    confidence_level: float = 0.95,
    method: str = 'historical'
) -> float:
    """Calculate Conditional Value at Risk (CVaR / Expected Shortfall).
    
    Parameters
    ----------
    returns : pd.Series
        Returns time series
    confidence_level : float, default 0.95
        Confidence level
    method : str, default 'historical'
        Calculation method ('historical' or 'parametric')
        
    Returns
    -------
    float
        CVaR as decimal (average loss beyond VaR)
    """
    var = calculate_var(returns, confidence_level, method)
    
    if method == 'historical':
        return returns[returns <= var].mean()
    
    elif method == 'parametric':
        mean = returns.mean()
        std = returns.std()
        z = stats.norm.ppf(1 - confidence_level)
        return mean - std * stats.norm.pdf(z) / (1 - confidence_level)
    
    else:
        raise ValueError(f"Unknown method: {method}")


def calculate_downside_risk(
    returns: pd.Series,
    target_return: float = 0.0,
    periods_per_year: int = 252
) -> Dict[str, float]:
    """Calculate downside risk metrics.
    
    Parameters
    ----------
    returns : pd.Series
        Returns time series
    target_return : float, default 0.0
        Target return threshold
    periods_per_year : int, default 252
        Periods per year for annualization
        
    Returns
    -------
    dict
        Dictionary with downside risk metrics
    """
    downside_returns = returns[returns < target_return] - target_return
    
    return {
        'downside_deviation': downside_returns.std() * np.sqrt(periods_per_year),
        'downside_frequency': len(downside_returns) / len(returns),
        'average_downside': downside_returns.mean(),
        'max_downside': downside_returns.min()
    }


def monte_carlo_simulation(
    returns: pd.Series,
    n_simulations: int = 10000,
    time_horizon: int = 252,
    initial_value: float = 100000.0,
    method: str = 'bootstrap'
) -> np.ndarray:
    """Run Monte Carlo simulation for portfolio value distribution.
    
    Parameters
    ----------
    returns : pd.Series
        Historical returns
    n_simulations : int, default 10000
        Number of simulation paths
    time_horizon : int, default 252
        Number of periods to simulate
    initial_value : float, default 100000.0
        Starting portfolio value
    method : str, default 'bootstrap'
        Simulation method ('bootstrap' or 'parametric')
        
    Returns
    -------
    np.ndarray
        Array of simulated ending values (shape: n_simulations)
        
    Examples
    --------
    >>> simulations = monte_carlo_simulation(returns, n_simulations=10000)
    >>> percentile_5 = np.percentile(simulations, 5)
    >>> print(f"5th percentile outcome: ${percentile_5:,.2f}")
    """
    if method == 'bootstrap':
        # Bootstrap resampling from historical returns
        simulated_returns = np.random.choice(
            returns.dropna(),
            size=(n_simulations, time_horizon),
            replace=True
        )
    
    elif method == 'parametric':
        # Parametric (normal distribution)
        mean = returns.mean()
        std = returns.std()
        simulated_returns = np.random.normal(
            mean,
            std,
            size=(n_simulations, time_horizon)
        )
    
    else:
        raise ValueError(f"Unknown method: {method}. Use 'bootstrap' or 'parametric'")
    
    # Calculate cumulative returns
    ending_values = initial_value * np.prod(1 + simulated_returns, axis=1)
    
    return ending_values


def stress_test(
    returns: pd.Series,
    scenarios: Optional[Dict[str, Dict[str, float]]] = None
) -> pd.DataFrame:
    """Run stress test scenarios on portfolio.
    
    Parameters
    ----------
    returns : pd.Series
        Historical returns
    scenarios : dict, optional
        Custom scenarios. If None, uses default historical scenarios.
        Format: {'scenario_name': {'mean_shock': -0.05, 'vol_multiplier': 2.0}}
        
    Returns
    -------
    pd.DataFrame
        Stress test results with scenario outcomes
        
    Examples
    --------
    >>> results = stress_test(returns)
    >>> print(results)
                         mean_return  volatility  var_95  cvar_95
    2008 Crisis              -0.45        0.65   -0.08    -0.12
    COVID Crash              -0.35        0.55   -0.06    -0.09
    """
    if scenarios is None:
        # Default historical stress scenarios
        scenarios = {
            '2008 Financial Crisis': {'mean_shock': -0.45, 'vol_multiplier': 2.5},
            'COVID-19 Crash (Mar 2020)': {'mean_shock': -0.35, 'vol_multiplier': 2.0},
            'Flash Crash (2010)': {'mean_shock': -0.10, 'vol_multiplier': 3.0},
            'Dot-com Bubble (2000-2002)': {'mean_shock': -0.40, 'vol_multiplier': 1.8},
            'Black Monday (1987)': {'mean_shock': -0.20, 'vol_multiplier': 3.5}
        }
    
    results = []
    
    for scenario_name, params in scenarios.items():
        # Apply shock to returns
        mean_shock = params.get('mean_shock', 0)
        vol_multiplier = params.get('vol_multiplier', 1.0)
        
        stressed_returns = returns * vol_multiplier + mean_shock / 252
        
        # Calculate metrics
        from portfolio_toolkit.metrics import calculate_volatility
        
        result = {
            'scenario': scenario_name,
            'mean_return': stressed_returns.mean() * 252,
            'volatility': calculate_volatility(stressed_returns, annualize=True),
            'var_95': calculate_var(stressed_returns, 0.95, 'historical'),
            'cvar_95': calculate_cvar(stressed_returns, 0.95, 'historical'),
            'max_loss': stressed_returns.min()
        }
        
        results.append(result)
    
    return pd.DataFrame(results).set_index('scenario')


def calculate_correlation_matrix(
    returns_df: pd.DataFrame,
    method: str = 'pearson'
) -> pd.DataFrame:
    """Calculate correlation matrix for portfolio positions.
    
    Parameters
    ----------
    returns_df : pd.DataFrame
        DataFrame with returns for multiple assets (columns = assets)
    method : str, default 'pearson'
        Correlation method ('pearson', 'spearman', 'kendall')
        
    Returns
    -------
    pd.DataFrame
        Correlation matrix
    """
    return returns_df.corr(method=method)


def calculate_portfolio_var_components(
    returns_df: pd.DataFrame,
    weights: np.ndarray,
    confidence_level: float = 0.95
) -> pd.DataFrame:
    """Calculate VaR contribution by position.
    
    Parameters
    ----------
    returns_df : pd.DataFrame
        Returns for each position (columns = positions)
    weights : np.ndarray
        Portfolio weights for each position
    confidence_level : float, default 0.95
        Confidence level for VaR
        
    Returns
    -------
    pd.DataFrame
        VaR contributions by position
    """
    # Calculate portfolio returns
    portfolio_returns = (returns_df * weights).sum(axis=1)
    
    # Portfolio VaR
    portfolio_var = calculate_var(portfolio_returns, confidence_level)
    
    # Marginal VaR for each position
    marginal_var = []
    
    for i, col in enumerate(returns_df.columns):
        # Correlation with portfolio
        correlation = returns_df[col].corr(portfolio_returns)
        
        # Position volatility
        position_vol = returns_df[col].std()
        
        # Marginal VaR
        mvar = correlation * position_vol / portfolio_returns.std() * portfolio_var
        
        marginal_var.append({
            'position': col,
            'weight': weights[i],
            'marginal_var': mvar,
            'var_contribution': mvar * weights[i],
            'var_pct': (mvar * weights[i]) / portfolio_var if portfolio_var != 0 else 0
        })
    
    return pd.DataFrame(marginal_var)


def calculate_risk_metrics(
    returns: pd.Series,
    confidence_level: float = 0.95,
    periods_per_year: int = 252
) -> Dict[str, Union[float, Dict]]:
    """Calculate comprehensive risk metrics.
    
    Parameters
    ----------
    returns : pd.Series
        Returns time series
    confidence_level : float, default 0.95
        Confidence level for VaR/CVaR
    periods_per_year : int, default 252
        Periods per year
        
    Returns
    -------
    dict
        Dictionary of risk metrics
    """
    from portfolio_toolkit.metrics import calculate_volatility
    
    return {
        'volatility': calculate_volatility(returns, periods_per_year),
        'var_95_historical': calculate_var(returns, confidence_level, 'historical'),
        'var_95_parametric': calculate_var(returns, confidence_level, 'parametric'),
        'cvar_95': calculate_cvar(returns, confidence_level),
        'downside_risk': calculate_downside_risk(returns, periods_per_year=periods_per_year),
        'skewness': returns.skew(),
        'kurtosis': returns.kurtosis(),
        'worst_day': returns.min(),
        'best_day': returns.max()
    }
