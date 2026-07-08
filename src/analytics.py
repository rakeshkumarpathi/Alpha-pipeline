import os

import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import create_engine

from quality import data_quality_report
from queries import QUERIES
from dashboard import display_dashboard
from datetime import datetime
from visualization import generate_dashboard

'''from visualization import (
    plot_close_price,
    plot_moving_average,
    plot_volume,
    plot_daily_return,
    plot_volatility
)'''
# Load environment variables
load_dotenv()

# Database connection details
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")

# Create database connection
engine = create_engine(
    f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

# Read the complete table
df = pd.read_sql("SELECT * FROM stock_features;", engine)

# Data quality checks
data_quality_report(df)

# SQL Analytics
for title, query in QUERIES.items():
    print(f"\n{'=' * 50}")
    print(title)
    print("=" * 50)

    result = pd.read_sql(query, engine)
    print(result)

# Dashboard Metrics
metrics = {
    "Symbol": df["symbol"].iloc[0],
    "Trading Days": len(df),
    "Date Range": f"{df['trade_date'].min()} → {df['trade_date'].max()}",
    "Generated On": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    "Highest Close": (f"${df['close_price'].max():.2f}"),
    "Lowest Close": (f"${df['close_price'].min():.2f}"),
    "Average Close": (f"${df['close_price'].mean():.2f}"),
    "Average Volume": f"{int(df['volume'].mean()):,}",
    "Highest Return": f"{df['daily_return'].max() * 100:.2f}%",
    "Highest Volatility": f"{df['volatility'].max() * 100:.2f}%"
}

# Display Dashboard
display_dashboard(metrics)

# Visualization
'''plot_close_price(df)

plot_moving_average(df)

plot_volume(df)

plot_daily_return(df)

plot_volatility(df)'''

generate_dashboard(df, metrics)