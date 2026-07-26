import pandas as pd
import ta
import os

# -------------------------------
# Load Gold Layer
# -------------------------------

df = pd.read_parquet("data/gold/AAPL_features.parquet")

# Ensure Date is datetime
df.index = pd.to_datetime(df.index)

print("Original Shape :", df.shape)

# ----------------------------------------------------
# Trend Indicators
# ----------------------------------------------------

# EMA 10
df["EMA_10"] = ta.trend.ema_indicator(
    close=df["Close"],
    window=10
)

# EMA 20
df["EMA_20"] = ta.trend.ema_indicator(
    close=df["Close"],
    window=20
)

# EMA 50
df["EMA_50"] = ta.trend.ema_indicator(
    close=df["Close"],
    window=50
)

# ----------------------------------------------------
# Momentum Indicators
# ----------------------------------------------------

# RSI
df["RSI_14"] = ta.momentum.rsi(
    close=df["Close"],
    window=14
)

# MACD
macd = ta.trend.MACD(close=df["Close"])

df["MACD"] = macd.macd()
df["MACD_Signal"] = macd.macd_signal()
df["MACD_Hist"] = macd.macd_diff()

# ----------------------------------------------------
# Volatility Indicators
# ----------------------------------------------------

bollinger = ta.volatility.BollingerBands(
    close=df["Close"],
    window=20,
    window_dev=2
)

df["BB_Upper"] = bollinger.bollinger_hband()
df["BB_Middle"] = bollinger.bollinger_mavg()
df["BB_Lower"] = bollinger.bollinger_lband()

# ----------------------------------------------------
# Remove rows containing NaN
# ----------------------------------------------------

df = df.dropna()

print("After Feature Engineering :", df.shape)

# ----------------------------------------------------
# Save Dataset
# ----------------------------------------------------

os.makedirs("data/ml", exist_ok=True)

output_path = "data/ml/AAPL_ml.parquet"

df.to_parquet(output_path)

print("\nSaved:", output_path)

# Preview
print("\nColumns:\n")
print(df.columns.tolist())

print("\nFirst Five Rows:\n")
print(df.head())