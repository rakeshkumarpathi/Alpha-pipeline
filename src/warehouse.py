import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy import text


def load_gold_to_postgres():

    # Read Gold Layer
    df = pd.read_parquet(
        "data/gold/AAPL_features.parquet"
    )

    df = df.reset_index() # Reset index to get 'Date' as a column

    # Add symbol
    df["symbol"] = "AAPL"

    # Rename columns
    df = df.rename(columns={
        "Date": "trade_date",
        "Open": "open_price",
        "High": "high_price",
        "Low": "low_price",
        "Close": "close_price",
        "Volume": "volume",
        "MA_5": "ma_5",
        "MA_20": "ma_20",
        "Daily_Return": "daily_return",
        "Volatility": "volatility"
    })

    # Keep only warehouse columns
    df = df[
        [
            "symbol",
            "trade_date",
            "open_price",
            "high_price",
            "low_price",
            "close_price",
            "volume",
            "ma_5",
            "ma_20",
            "daily_return",
            "volatility"
        ]
    ]

    # PostgreSQL Connection
    engine = create_engine(
        "postgresql://postgres:alpha@localhost:5432/Alphapipeline"
    )

    # Clear old data first
    with engine.begin() as conn:
        conn.execute(text("TRUNCATE TABLE stock_features RESTART IDENTITY"))

    # Load new data
    df.to_sql(
        "stock_features",
        engine,
        if_exists="append",
        index=False
    )

    print(f"{len(df)} rows loaded successfully.")
    print(df.columns.tolist())
    print(df.shape)