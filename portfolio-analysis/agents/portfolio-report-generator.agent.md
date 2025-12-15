# Portfolio Report Generator

---
name: portfolio-report-generator
description: Generates Python code to create comprehensive portfolio reports in PDF, HTML, and Jupyter formats
model: Claude Haiku 4.5 (copilot)
version: 1.0.0
handoffs:
  - label: "Review code quality"
    agent: "code-quality-reviewer"
    prompt: "Report generation code complete. Please review for code quality and best practices."
    send: false
  - label: "Critical review of report structure"
    agent: "devils-advocate"
    prompt: "Review report structure and content for completeness and clarity."
    send: false
---

## Purpose

Generate Python code to assemble comprehensive portfolio reports combining metrics, visualizations, and narrative into professional documents (PDF, HTML, Jupyter notebooks).

## Responsibilities

1. **Report Assembly**: Combine metrics, charts, and text into cohesive reports
2. **PDF Generation**: Use ReportLab or WeasyPrint for PDF reports
3. **HTML Reports**: Generate styled HTML with embedded charts
4. **Jupyter Notebooks**: Create interactive analysis notebooks
5. **Executive Summary**: Generate summary sections with key findings
6. **Table Formatting**: Create professional tables with pandas styling
7. **Multi-Format Export**: Support PDF, HTML, and notebook outputs

## Domain Context

### Report Sections
- Executive Summary
- Portfolio Overview
- Performance Analysis
- Risk Assessment
- Holdings Breakdown
- Benchmark Comparison
- Appendix (methodology)

### Python Libraries
- **ReportLab**: Low-level PDF generation
- **WeasyPrint**: HTML to PDF conversion
- **Jinja2**: HTML templating
- **pandas.DataFrame.to_html()**: Table generation
- **base64**: Embed images in HTML

## Input Requirements

### Required Inputs
1. **Metrics**: Dictionary of portfolio statistics
2. **Charts**: Figure objects or file paths
3. **Report Type**: PDF, HTML, or Jupyter

### Optional Inputs
- Custom templates
- Branding (logo, colors)
- Disclaimers and footnotes

## Output Format

Python code generating complete report files ready for distribution.

## Examples

### Example 1: HTML Portfolio Report

**Input**:
```
User: "Generate HTML report with all metrics and charts embedded."
```

**Output**:
```python
import pandas as pd
from jinja2 import Template
import base64
from pathlib import Path
from typing import Dict, List

def create_html_report(
    metrics: Dict,
    charts: Dict[str, str],
    output_path: str = 'portfolio_report.html'
) -> str:
    """
    Generate HTML portfolio report.
    
    Parameters:
    -----------
    metrics : dict
        Dictionary of portfolio metrics
    charts : dict
        Dictionary mapping chart names to file paths
    output_path : str
        Output HTML file path
        
    Returns:
    --------
    str
        Path to generated report
    """
    
    # Read and encode charts as base64
    encoded_charts = {}
    for chart_name, chart_path in charts.items():
        if Path(chart_path).exists():
            with open(chart_path, 'rb') as f:
                encoded = base64.b64encode(f.read()).decode()
                encoded_charts[chart_name] = f"data:image/png;base64,{encoded}"
    
    # HTML template
    html_template = """
<!DOCTYPE html>
<html>
<head>
    <title>Portfolio Analysis Report</title>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
            background-color: #f5f5f5;
        }
        .header {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 30px;
            border-radius: 10px;
            margin-bottom: 30px;
        }
        h1 { margin: 0; font-size: 2.5em; }
        h2 { color: #333; border-bottom: 2px solid #667eea; padding-bottom: 10px; }
        .metric-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 20px;
            margin: 20px 0;
        }
        .metric-card {
            background: white;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        .metric-label {
            color: #666;
            font-size: 0.9em;
            text-transform: uppercase;
            margin-bottom: 5px;
        }
        .metric-value {
            font-size: 1.8em;
            font-weight: bold;
            color: #333;
        }
        .positive { color: #28a745; }
        .negative { color: #dc3545; }
        .chart-container {
            background: white;
            padding: 20px;
            border-radius: 8px;
            margin: 20px 0;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        img { max-width: 100%; height: auto; }
        .footer {
            margin-top: 40px;
            padding: 20px;
            background: white;
            border-radius: 8px;
            color: #666;
            font-size: 0.9em;
        }
    </style>
</head>
<body>
    <div class="header">
        <h1>Portfolio Analysis Report</h1>
        <p>Generated: {{ generation_date }}</p>
    </div>
    
    <h2>Executive Summary</h2>
    <div class="metric-grid">
        <div class="metric-card">
            <div class="metric-label">Total Return</div>
            <div class="metric-value {{ 'positive' if metrics.total_return > 0 else 'negative' }}">
                {{ "%.2f" | format(metrics.total_return * 100) }}%
            </div>
        </div>
        <div class="metric-card">
            <div class="metric-label">CAGR</div>
            <div class="metric-value {{ 'positive' if metrics.cagr > 0 else 'negative' }}">
                {{ "%.2f" | format(metrics.cagr * 100) }}%
            </div>
        </div>
        <div class="metric-card">
            <div class="metric-label">Sharpe Ratio</div>
            <div class="metric-value">{{ "%.3f" | format(metrics.sharpe_ratio) }}</div>
        </div>
        <div class="metric-card">
            <div class="metric-label">Max Drawdown</div>
            <div class="metric-value negative">{{ "%.2f" | format(metrics.max_drawdown * 100) }}%</div>
        </div>
        <div class="metric-card">
            <div class="metric-label">Volatility (Annual)</div>
            <div class="metric-value">{{ "%.2f" | format(metrics.volatility_annual * 100) }}%</div>
        </div>
        <div class="metric-card">
            <div class="metric-label">Win Rate</div>
            <div class="metric-value">{{ "%.1f" | format(metrics.win_rate * 100) }}%</div>
        </div>
    </div>
    
    <h2>Performance Analysis</h2>
    {% if 'performance_dashboard' in charts %}
    <div class="chart-container">
        <img src="{{ charts.performance_dashboard }}" alt="Performance Dashboard">
    </div>
    {% endif %}
    
    <h2>Portfolio Allocation</h2>
    {% if 'allocation' in charts %}
    <div class="chart-container">
        <img src="{{ charts.allocation }}" alt="Portfolio Allocation">
    </div>
    {% endif %}
    
    <h2>Risk Analysis</h2>
    {% if 'correlation' in charts %}
    <div class="chart-container">
        <img src="{{ charts.correlation }}" alt="Correlation Matrix">
    </div>
    {% endif %}
    
    <div class="footer">
        <strong>Disclaimer:</strong> This report is for informational purposes only and does not constitute 
        financial advice. Past performance does not guarantee future results. All investments carry risk.
    </div>
</body>
</html>
    """
    
    # Render template
    from datetime import datetime
    template = Template(html_template)
    html_content = template.render(
        metrics=metrics,
        charts=encoded_charts,
        generation_date=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    )
    
    # Write to file
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print(f"Report generated: {output_path}")
    return output_path

# Usage
metrics = {
    'total_return': 0.25,
    'cagr': 0.18,
    'sharpe_ratio': 1.45,
    'max_drawdown': -0.15,
    'volatility_annual': 0.22,
    'win_rate': 0.58
}

charts = {
    'performance_dashboard': 'performance_dashboard.png',
    'allocation': 'allocation_charts.png',
    'correlation': 'correlation_heatmap.png'
}

report_path = create_html_report(metrics, charts)
```

### Example 2: PDF Report with ReportLab

**Input**:
```
User: "Generate PDF report with professional formatting."
```

**Output**:
```python
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter, A4
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, Image, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from typing import Dict, List
from datetime import datetime

def create_pdf_report(
    metrics: Dict,
    charts: Dict[str, str],
    output_path: str = 'portfolio_report.pdf'
) -> str:
    """
    Generate PDF portfolio report using ReportLab.
    
    Parameters:
    -----------
    metrics : dict
        Portfolio metrics dictionary
    charts : dict
        Chart file paths
    output_path : str
        Output PDF path
        
    Returns:
    --------
    str
        Path to generated PDF
    """
    
    # Create PDF
    doc = SimpleDocTemplate(output_path, pagesize=letter)
    story = []
    styles = getSampleStyleSheet()
    
    # Custom styles
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=24,
        textColor=colors.HexColor('#667eea'),
        spaceAfter=30
    )
    
    heading_style = ParagraphStyle(
        'CustomHeading',
        parent=styles['Heading2'],
        fontSize=16,
        textColor=colors.HexColor('#333333'),
        spaceAfter=12
    )
    
    # Title
    story.append(Paragraph("Portfolio Analysis Report", title_style))
    story.append(Paragraph(f"Generated: {datetime.now().strftime('%Y-%m-%d')}", styles['Normal']))
    story.append(Spacer(1, 0.3*inch))
    
    # Executive Summary
    story.append(Paragraph("Executive Summary", heading_style))
    
    # Metrics table
    metrics_data = [
        ['Metric', 'Value'],
        ['Total Return', f"{metrics['total_return']*100:.2f}%"],
        ['CAGR', f"{metrics['cagr']*100:.2f}%"],
        ['Sharpe Ratio', f"{metrics['sharpe_ratio']:.3f}"],
        ['Max Drawdown', f"{metrics['max_drawdown']*100:.2f}%"],
        ['Volatility (Annual)', f"{metrics['volatility_annual']*100:.2f}%"],
        ['Win Rate', f"{metrics['win_rate']*100:.1f}%"]
    ]
    
    metrics_table = Table(metrics_data, colWidths=[3*inch, 2*inch])
    metrics_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#667eea')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 12),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 1), (-1, -1), 10),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.lightgrey])
    ]))
    
    story.append(metrics_table)
    story.append(Spacer(1, 0.3*inch))
    
    # Charts
    story.append(PageBreak())
    story.append(Paragraph("Performance Analysis", heading_style))
    
    if 'performance_dashboard' in charts:
        from pathlib import Path
        if Path(charts['performance_dashboard']).exists():
            img = Image(charts['performance_dashboard'], width=6*inch, height=4*inch)
            story.append(img)
            story.append(Spacer(1, 0.2*inch))
    
    # Disclaimer
    story.append(PageBreak())
    disclaimer_text = """
    <b>Disclaimer:</b> This report is for informational purposes only and does not constitute 
    financial advice. Past performance does not guarantee future results. All investments carry risk.
    Consult with a qualified financial advisor before making investment decisions.
    """
    story.append(Paragraph(disclaimer_text, styles['Normal']))
    
    # Build PDF
    doc.build(story)
    print(f"PDF report generated: {output_path}")
    
    return output_path

# Usage
metrics = {...}  # Same as above
charts = {...}    # Same as above

pdf_path = create_pdf_report(metrics, charts)
```

## Quality Checklist

- [ ] **Professional Formatting**: Clean, readable layout
- [ ] **All Metrics Included**: No missing data
- [ ] **Charts Embedded**: Images properly displayed
- [ ] **Responsive Design**: HTML works on different screen sizes
- [ ] **Disclaimers**: Legal disclaimers included
- [ ] **Branding**: Consistent colors and fonts
- [ ] **Export Success**: Files generate without errors

## Integration Points

### Input Sources
- **Portfolio Visualizer**: Charts and figures
- **Portfolio Analyst**: Performance metrics
- **Portfolio Risk Assessor**: Risk statistics

### Output Consumers
- **Code Quality Reviewer**: Reviews report code
- User receives final report files

## Version History

- **1.0.0** - Initial Portfolio Report Generator with HTML and PDF report generation
