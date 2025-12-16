"""Portfolio Analysis Toolkit - A comprehensive library for portfolio analysis.

This library provides functions for:
- Data loading and cleaning (data module)
- Financial metrics calculation (metrics module)
- Risk assessment (risk module)
- Visualizations (viz module)
- Report generation (reports module)
"""

__version__ = "2.0.0"
__author__ = "Portfolio Analysis Agent Group"

from portfolio_toolkit import data, metrics, risk, viz, reports

__all__ = ['data', 'metrics', 'risk', 'viz', 'reports']
