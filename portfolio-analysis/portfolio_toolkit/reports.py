"""Portfolio report generation in HTML and PDF formats.

This module provides functions for assembling comprehensive portfolio reports
combining metrics, visualizations, and narrative.
"""

import pandas as pd
from typing import Dict, List, Optional, Union
from pathlib import Path
from datetime import datetime


def generate_html_report(
    metrics: Dict,
    chart_paths: Dict[str, str],
    output_path: str = 'portfolio_report.html',
    title: str = 'Portfolio Analysis Report',
    subtitle: Optional[str] = None
) -> str:
    """Generate HTML portfolio report with embedded charts.
    
    Parameters
    ----------
    metrics : dict
        Dictionary of portfolio metrics and statistics
    chart_paths : dict
        Dictionary mapping chart names to file paths
    output_path : str, default 'portfolio_report.html'
        Output HTML file path
    title : str, default 'Portfolio Analysis Report'
        Report title
    subtitle : str, optional
        Report subtitle or date range
        
    Returns
    -------
    str
        Path to generated HTML file
        
    Examples
    --------
    >>> metrics = {'sharpe_ratio': 1.5, 'max_drawdown': -0.15}
    >>> charts = {'cumulative': 'cumulative_returns.png'}
    >>> report_path = generate_html_report(metrics, charts)
    """
    if subtitle is None:
        subtitle = f"Generated on {datetime.now().strftime('%Y-%m-%d %H:%M')}"
    
    # HTML template
    html_template = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{title}</title>
        <style>
            body {{
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                margin: 40px;
                background-color: #f5f5f5;
                color: #333;
            }}
            .container {{
                max-width: 1200px;
                margin: 0 auto;
                background-color: white;
                padding: 40px;
                box-shadow: 0 0 10px rgba(0,0,0,0.1);
            }}
            h1 {{
                color: #2c3e50;
                border-bottom: 3px solid #3498db;
                padding-bottom: 10px;
            }}
            h2 {{
                color: #34495e;
                margin-top: 30px;
                border-left: 4px solid #3498db;
                padding-left: 10px;
            }}
            .subtitle {{
                color: #7f8c8d;
                font-size: 14px;
                margin-bottom: 30px;
            }}
            .metrics-grid {{
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
                gap: 20px;
                margin: 20px 0;
            }}
            .metric-card {{
                background-color: #ecf0f1;
                padding: 20px;
                border-radius: 8px;
                border-left: 4px solid #3498db;
            }}
            .metric-label {{
                font-size: 14px;
                color: #7f8c8d;
                text-transform: uppercase;
            }}
            .metric-value {{
                font-size: 24px;
                font-weight: bold;
                color: #2c3e50;
                margin-top: 5px;
            }}
            .metric-value.positive {{
                color: #27ae60;
            }}
            .metric-value.negative {{
                color: #e74c3c;
            }}
            .chart {{
                margin: 20px 0;
                text-align: center;
            }}
            .chart img {{
                max-width: 100%;
                height: auto;
                border: 1px solid #ddd;
                border-radius: 4px;
            }}
            table {{
                width: 100%;
                border-collapse: collapse;
                margin: 20px 0;
            }}
            th, td {{
                text-align: left;
                padding: 12px;
                border-bottom: 1px solid #ddd;
            }}
            th {{
                background-color: #3498db;
                color: white;
            }}
            tr:hover {{
                background-color: #f5f5f5;
            }}
            .disclaimer {{
                margin-top: 40px;
                padding: 20px;
                background-color: #fff3cd;
                border-left: 4px solid #ffc107;
                font-size: 12px;
                color: #856404;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>{title}</h1>
            <div class="subtitle">{subtitle}</div>
            
            <h2>Executive Summary</h2>
            <div class="metrics-grid">
                {_format_metrics_html(metrics)}
            </div>
            
            <h2>Performance Analysis</h2>
            {_format_charts_html(chart_paths)}
            
            <h2>Risk Metrics</h2>
            {_format_risk_table_html(metrics)}
            
            <div class="disclaimer">
                <strong>Disclaimer:</strong> This report is for informational purposes only 
                and does not constitute investment advice. Past performance is not indicative 
                of future results. All investments involve risk, including possible loss of principal.
            </div>
        </div>
    </body>
    </html>
    """
    
    # Write HTML file
    output_path = Path(output_path)
    output_path.write_text(html_template)
    
    return str(output_path)


def _format_metrics_html(metrics: Dict) -> str:
    """Format metrics as HTML cards."""
    html = ""
    
    # Define key metrics to display
    display_metrics = {
        'total_return': 'Total Return',
        'cagr': 'CAGR',
        'sharpe_ratio': 'Sharpe Ratio',
        'volatility': 'Volatility',
        'max_drawdown': 'Max Drawdown',
        'sortino_ratio': 'Sortino Ratio'
    }
    
    for key, label in display_metrics.items():
        if key in metrics:
            value = metrics[key]
            
            # Format value
            if key in ['total_return', 'cagr', 'volatility', 'max_drawdown']:
                formatted_value = f"{value:.2%}"
                value_class = "positive" if value > 0 else "negative"
            else:
                formatted_value = f"{value:.2f}"
                value_class = "positive" if value > 0 else "negative"
            
            html += f"""
            <div class="metric-card">
                <div class="metric-label">{label}</div>
                <div class="metric-value {value_class}">{formatted_value}</div>
            </div>
            """
    
    return html


def _format_charts_html(chart_paths: Dict[str, str]) -> str:
    """Format charts as HTML with embedded images."""
    html = ""
    
    for chart_name, path in chart_paths.items():
        if Path(path).exists():
            html += f"""
            <div class="chart">
                <h3>{chart_name.replace('_', ' ').title()}</h3>
                <img src="{path}" alt="{chart_name}">
            </div>
            """
    
    return html


def _format_risk_table_html(metrics: Dict) -> str:
    """Format risk metrics as HTML table."""
    risk_metrics = {
        'volatility': 'Volatility (Annual)',
        'var_95_historical': '95% VaR (Historical)',
        'cvar_95': '95% CVaR',
        'skewness': 'Skewness',
        'kurtosis': 'Kurtosis'
    }
    
    html = "<table><thead><tr><th>Metric</th><th>Value</th></tr></thead><tbody>"
    
    for key, label in risk_metrics.items():
        if key in metrics:
            value = metrics[key]
            
            # Format based on metric type
            if key in ['volatility', 'var_95_historical', 'cvar_95']:
                formatted = f"{value:.2%}"
            else:
                formatted = f"{value:.2f}"
            
            html += f"<tr><td>{label}</td><td>{formatted}</td></tr>"
    
    html += "</tbody></table>"
    return html


def generate_markdown_report(
    metrics: Dict,
    output_path: str = 'portfolio_report.md',
    title: str = 'Portfolio Analysis Report'
) -> str:
    """Generate Markdown portfolio report.
    
    Parameters
    ----------
    metrics : dict
        Dictionary of portfolio metrics
    output_path : str, default 'portfolio_report.md'
        Output markdown file path
    title : str, default 'Portfolio Analysis Report'
        Report title
        
    Returns
    -------
    str
        Path to generated markdown file
    """
    md_content = f"""# {title}

**Generated**: {datetime.now().strftime('%Y-%m-%d %H:%M')}

## Executive Summary

"""
    
    # Add key metrics
    if 'total_return' in metrics:
        md_content += f"- **Total Return**: {metrics['total_return']:.2%}\n"
    if 'cagr' in metrics:
        md_content += f"- **CAGR**: {metrics['cagr']:.2%}\n"
    if 'sharpe_ratio' in metrics:
        md_content += f"- **Sharpe Ratio**: {metrics['sharpe_ratio']:.2f}\n"
    if 'max_drawdown' in metrics:
        md_content += f"- **Max Drawdown**: {metrics['max_drawdown']:.2%}\n"
    
    md_content += "\n## Performance Metrics\n\n"
    md_content += "| Metric | Value |\n"
    md_content += "|--------|-------|\n"
    
    for key, value in metrics.items():
        if isinstance(value, (int, float)):
            if key in ['total_return', 'cagr', 'volatility', 'max_drawdown']:
                formatted = f"{value:.2%}"
            else:
                formatted = f"{value:.2f}"
            
            label = key.replace('_', ' ').title()
            md_content += f"| {label} | {formatted} |\n"
    
    md_content += "\n## Disclaimer\n\n"
    md_content += "This report is for informational purposes only and does not constitute investment advice.\n"
    
    # Write markdown file
    output_path = Path(output_path)
    output_path.write_text(md_content)
    
    return str(output_path)


def generate_metrics_dataframe(metrics: Dict) -> pd.DataFrame:
    """Convert metrics dictionary to DataFrame for export.
    
    Parameters
    ----------
    metrics : dict
        Portfolio metrics dictionary
        
    Returns
    -------
    pd.DataFrame
        Metrics as DataFrame
    """
    # Flatten nested dictionaries
    flat_metrics = {}
    
    for key, value in metrics.items():
        if isinstance(value, dict):
            for subkey, subvalue in value.items():
                flat_metrics[f"{key}_{subkey}"] = subvalue
        else:
            flat_metrics[key] = value
    
    df = pd.DataFrame([flat_metrics])
    return df.T.rename(columns={0: 'value'})


def export_metrics_to_excel(
    metrics: Dict,
    output_path: str = 'portfolio_metrics.xlsx'
) -> str:
    """Export metrics to Excel file.
    
    Parameters
    ----------
    metrics : dict
        Portfolio metrics
    output_path : str, default 'portfolio_metrics.xlsx'
        Output Excel file path
        
    Returns
    -------
    str
        Path to Excel file
    """
    df = generate_metrics_dataframe(metrics)
    df.to_excel(output_path)
    return output_path
