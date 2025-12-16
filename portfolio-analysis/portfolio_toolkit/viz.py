"""Portfolio visualization functions using matplotlib and seaborn.

This module provides functions for creating publication-quality charts including
performance plots, risk visualizations, and allocation breakdowns.
"""

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
from typing import Optional, Tuple, List, Dict
import warnings


# Set publication-quality defaults
plt.rcParams['figure.figsize'] = (12, 6)
plt.rcParams['figure.dpi'] = 100
plt.rcParams['font.size'] = 10
plt.rcParams['axes.grid'] = True
plt.rcParams['grid.alpha'] = 0.3


def plot_cumulative_returns(
    returns: pd.Series,
    benchmark_returns: Optional[pd.Series] = None,
    figsize: Tuple[int, int] = (12, 6),
    title: str = 'Cumulative Returns'
) -> plt.Figure:
    """Plot cumulative returns over time.
    
    Parameters
    ----------
    returns : pd.Series
        Portfolio returns
    benchmark_returns : pd.Series, optional
        Benchmark returns for comparison
    figsize : tuple, default (12, 6)
        Figure size (width, height)
    title : str, default 'Cumulative Returns'
        Chart title
        
    Returns
    -------
    matplotlib.figure.Figure
        Figure object
        
    Examples
    --------
    >>> fig = plot_cumulative_returns(returns, benchmark_returns)
    >>> fig.savefig('cumulative_returns.png', dpi=300, bbox_inches='tight')
    """
    fig, ax = plt.subplots(figsize=figsize)
    
    # Calculate cumulative returns
    cum_returns = (1 + returns).cumprod() - 1
    
    # Plot portfolio
    ax.plot(cum_returns.index, cum_returns.values, label='Portfolio', linewidth=2)
    
    # Plot benchmark if provided
    if benchmark_returns is not None:
        cum_benchmark = (1 + benchmark_returns).cumprod() - 1
        ax.plot(cum_benchmark.index, cum_benchmark.values, 
                label='Benchmark', linewidth=2, linestyle='--', alpha=0.7)
    
    ax.set_xlabel('Date')
    ax.set_ylabel('Cumulative Return')
    ax.set_title(title, fontsize=14, fontweight='bold')
    ax.legend(loc='upper left')
    ax.axhline(y=0, color='black', linestyle='-', linewidth=0.5, alpha=0.5)
    
    # Format y-axis as percentage
    ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda y, _: f'{y:.0%}'))
    
    plt.tight_layout()
    return fig


def plot_drawdown(
    prices: pd.Series,
    figsize: Tuple[int, int] = (12, 6),
    title: str = 'Drawdown'
) -> plt.Figure:
    """Plot drawdown chart showing peak-to-trough declines.
    
    Parameters
    ----------
    prices : pd.Series
        Price time series
    figsize : tuple, default (12, 6)
        Figure size
    title : str, default 'Drawdown'
        Chart title
        
    Returns
    -------
    matplotlib.figure.Figure
        Figure object
    """
    fig, ax = plt.subplots(figsize=figsize)
    
    # Calculate drawdown
    cumulative = prices / prices.iloc[0]
    running_max = cumulative.cummax()
    drawdown = (cumulative - running_max) / running_max
    
    # Plot
    ax.fill_between(drawdown.index, drawdown.values, 0, 
                     alpha=0.3, color='red', label='Drawdown')
    ax.plot(drawdown.index, drawdown.values, color='red', linewidth=1)
    
    ax.set_xlabel('Date')
    ax.set_ylabel('Drawdown')
    ax.set_title(title, fontsize=14, fontweight='bold')
    ax.axhline(y=0, color='black', linestyle='-', linewidth=0.5)
    
    # Format y-axis as percentage
    ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda y, _: f'{y:.0%}'))
    
    plt.tight_layout()
    return fig


def plot_rolling_metric(
    returns: pd.Series,
    metric_values: pd.Series,
    metric_name: str = 'Sharpe Ratio',
    figsize: Tuple[int, int] = (12, 6)
) -> plt.Figure:
    """Plot rolling metric over time.
    
    Parameters
    ----------
    returns : pd.Series
        Returns time series
    metric_values : pd.Series
        Pre-calculated rolling metric values
    metric_name : str, default 'Sharpe Ratio'
        Name of metric for labels
    figsize : tuple, default (12, 6)
        Figure size
        
    Returns
    -------
    matplotlib.figure.Figure
        Figure object
    """
    fig, ax = plt.subplots(figsize=figsize)
    
    ax.plot(metric_values.index, metric_values.values, linewidth=2)
    ax.set_xlabel('Date')
    ax.set_ylabel(metric_name)
    ax.set_title(f'Rolling {metric_name}', fontsize=14, fontweight='bold')
    ax.axhline(y=0, color='black', linestyle='-', linewidth=0.5, alpha=0.5)
    
    plt.tight_layout()
    return fig


def plot_return_distribution(
    returns: pd.Series,
    bins: int = 50,
    figsize: Tuple[int, int] = (12, 6),
    show_normal: bool = True
) -> plt.Figure:
    """Plot return distribution histogram with normal curve overlay.
    
    Parameters
    ----------
    returns : pd.Series
        Returns time series
    bins : int, default 50
        Number of histogram bins
    figsize : tuple, default (12, 6)
        Figure size
    show_normal : bool, default True
        Whether to overlay normal distribution
        
    Returns
    -------
    matplotlib.figure.Figure
        Figure object
    """
    fig, ax = plt.subplots(figsize=figsize)
    
    # Plot histogram
    n, bins_edges, patches = ax.hist(returns.dropna(), bins=bins, 
                                     alpha=0.7, edgecolor='black', 
                                     density=True, label='Actual')
    
    # Overlay normal distribution if requested
    if show_normal:
        mu = returns.mean()
        sigma = returns.std()
        x = np.linspace(returns.min(), returns.max(), 100)
        from scipy.stats import norm
        ax.plot(x, norm.pdf(x, mu, sigma), 'r-', linewidth=2, 
                label='Normal Distribution')
    
    ax.set_xlabel('Return')
    ax.set_ylabel('Density')
    ax.set_title('Return Distribution', fontsize=14, fontweight='bold')
    ax.legend()
    
    # Add statistics text
    stats_text = f'Mean: {returns.mean():.2%}\nStd: {returns.std():.2%}\nSkew: {returns.skew():.2f}\nKurt: {returns.kurtosis():.2f}'
    ax.text(0.02, 0.98, stats_text, transform=ax.transAxes, 
            fontsize=9, verticalalignment='top',
            bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))
    
    plt.tight_layout()
    return fig


def plot_correlation_heatmap(
    returns_df: pd.DataFrame,
    figsize: Tuple[int, int] = (10, 8),
    cmap: str = 'RdYlGn'
) -> plt.Figure:
    """Plot correlation heatmap for multiple assets.
    
    Parameters
    ----------
    returns_df : pd.DataFrame
        DataFrame with returns for multiple assets
    figsize : tuple, default (10, 8)
        Figure size
    cmap : str, default 'RdYlGn'
        Colormap name
        
    Returns
    -------
    matplotlib.figure.Figure
        Figure object
    """
    fig, ax = plt.subplots(figsize=figsize)
    
    # Calculate correlation matrix
    corr = returns_df.corr()
    
    # Plot heatmap
    sns.heatmap(corr, annot=True, fmt='.2f', cmap=cmap, 
                center=0, vmin=-1, vmax=1, square=True,
                linewidths=0.5, cbar_kws={'shrink': 0.8}, ax=ax)
    
    ax.set_title('Correlation Matrix', fontsize=14, fontweight='bold')
    
    plt.tight_layout()
    return fig


def plot_allocation_pie(
    weights: Dict[str, float],
    figsize: Tuple[int, int] = (10, 8),
    title: str = 'Portfolio Allocation'
) -> plt.Figure:
    """Plot portfolio allocation pie chart.
    
    Parameters
    ----------
    weights : dict
        Dictionary mapping asset names to weights
    figsize : tuple, default (10, 8)
        Figure size
    title : str, default 'Portfolio Allocation'
        Chart title
        
    Returns
    -------
    matplotlib.figure.Figure
        Figure object
    """
    fig, ax = plt.subplots(figsize=figsize)
    
    labels = list(weights.keys())
    sizes = list(weights.values())
    
    # Use colorblind-friendly palette
    colors = sns.color_palette('colorblind', len(labels))
    
    wedges, texts, autotexts = ax.pie(sizes, labels=labels, autopct='%1.1f%%',
                                       colors=colors, startangle=90)
    
    # Improve text readability
    for autotext in autotexts:
        autotext.set_color('white')
        autotext.set_fontweight('bold')
    
    ax.set_title(title, fontsize=14, fontweight='bold')
    
    plt.tight_layout()
    return fig


def plot_performance_dashboard(
    returns: pd.Series,
    benchmark_returns: Optional[pd.Series] = None,
    figsize: Tuple[int, int] = (14, 10)
) -> plt.Figure:
    """Create comprehensive performance dashboard with multiple panels.
    
    Parameters
    ----------
    returns : pd.Series
        Portfolio returns
    benchmark_returns : pd.Series, optional
        Benchmark returns
    figsize : tuple, default (14, 10)
        Figure size
        
    Returns
    -------
    matplotlib.figure.Figure
        Figure object with 4 subplots
    """
    fig = plt.figure(figsize=figsize)
    gs = fig.add_gridspec(2, 2, hspace=0.3, wspace=0.3)
    
    # 1. Cumulative returns
    ax1 = fig.add_subplot(gs[0, :])
    cum_returns = (1 + returns).cumprod() - 1
    ax1.plot(cum_returns.index, cum_returns.values, label='Portfolio', linewidth=2)
    if benchmark_returns is not None:
        cum_benchmark = (1 + benchmark_returns).cumprod() - 1
        ax1.plot(cum_benchmark.index, cum_benchmark.values, 
                label='Benchmark', linewidth=2, linestyle='--', alpha=0.7)
    ax1.set_title('Cumulative Returns', fontweight='bold')
    ax1.set_ylabel('Return')
    ax1.legend()
    ax1.yaxis.set_major_formatter(plt.FuncFormatter(lambda y, _: f'{y:.0%}'))
    ax1.grid(True, alpha=0.3)
    
    # 2. Drawdown
    ax2 = fig.add_subplot(gs[1, 0])
    prices = (1 + returns).cumprod()
    running_max = prices.cummax()
    drawdown = (prices - running_max) / running_max
    ax2.fill_between(drawdown.index, drawdown.values, 0, alpha=0.3, color='red')
    ax2.plot(drawdown.index, drawdown.values, color='red', linewidth=1)
    ax2.set_title('Drawdown', fontweight='bold')
    ax2.set_ylabel('Drawdown')
    ax2.yaxis.set_major_formatter(plt.FuncFormatter(lambda y, _: f'{y:.0%}'))
    ax2.grid(True, alpha=0.3)
    
    # 3. Return distribution
    ax3 = fig.add_subplot(gs[1, 1])
    ax3.hist(returns.dropna(), bins=50, alpha=0.7, edgecolor='black')
    ax3.set_title('Return Distribution', fontweight='bold')
    ax3.set_xlabel('Return')
    ax3.set_ylabel('Frequency')
    ax3.axvline(x=0, color='black', linestyle='--', linewidth=1)
    ax3.grid(True, alpha=0.3)
    
    fig.suptitle('Portfolio Performance Dashboard', fontsize=16, fontweight='bold', y=0.995)
    
    return fig


def save_figure(
    fig: plt.Figure,
    filepath: str,
    dpi: int = 300,
    format: Optional[str] = None
) -> str:
    """Save figure to file with publication quality.
    
    Parameters
    ----------
    fig : matplotlib.figure.Figure
        Figure to save
    filepath : str
        Output file path
    dpi : int, default 300
        Resolution in dots per inch
    format : str, optional
        File format ('png', 'pdf', 'svg'). If None, inferred from filepath
        
    Returns
    -------
    str
        Path to saved file
    """
    fig.savefig(filepath, dpi=dpi, format=format, bbox_inches='tight')
    plt.close(fig)
    return filepath
