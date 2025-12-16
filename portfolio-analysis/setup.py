"""Setup script for portfolio_toolkit library."""

from setuptools import setup, find_packages
from pathlib import Path

# Read README
readme_path = Path(__file__).parent / "README.md"
long_description = readme_path.read_text() if readme_path.exists() else ""

setup(
    name="portfolio_toolkit",
    version="2.0.0",
    description="Comprehensive toolkit for portfolio analysis and reporting",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Portfolio Analysis Agent Group",
    python_requires=">=3.8",
    packages=find_packages(),
    install_requires=[
        "pandas>=2.0.0",
        "numpy>=1.24.0",
        "matplotlib>=3.7.0",
        "seaborn>=0.12.0",
        "scipy>=1.10.0",
    ],
    extras_require={
        "data": [
            "yfinance>=0.2.28",
            "openpyxl>=3.0.0",  # For Excel support
        ],
        "reports": [
            "jinja2>=3.1.2",
            "reportlab>=4.0.0",
        ],
        "full": [
            "yfinance>=0.2.28",
            "openpyxl>=3.0.0",
            "jinja2>=3.1.2",
            "reportlab>=4.0.0",
            "plotly>=5.14.0",
        ],
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Financial and Insurance Industry",
        "Topic :: Office/Business :: Financial :: Investment",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    keywords="portfolio finance investment analysis risk metrics",
)
