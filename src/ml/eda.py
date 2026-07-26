import pandas as pd
import matplotlib.pyplot as plt

# Load Gold Layer
df = pd.read_parquet("data/gold/AAPL_features.parquet")

# -----------------------------
# Inspect Dataset
# -----------------------------
print("\nColumns:")
print(df.columns.tolist())

print("\nIndex:")
print(df.index)

print("\nFirst 5 Rows:")
print(df.head())

# -----------------------------
# Handle Date Column / Index
# -----------------------------
if "Date" in df.columns:
    df["Date"] = pd.to_datetime(df["Date"])
    df.set_index("Date", inplace=True)
else:
    # If Date is already the index, convert it to datetime
    df.index = pd.to_datetime(df.index)

# -----------------------------
# Close Price
# -----------------------------
plt.figure(figsize=(12, 5))
plt.plot(df.index, df["Close"])
plt.title("Close Price")
plt.xlabel("Date")
plt.ylabel("Price")
plt.grid(True)
plt.show()

# -----------------------------
# Trading Volume
# -----------------------------
plt.figure(figsize=(12, 5))
plt.plot(df.index, df["Volume"])
plt.title("Trading Volume")
plt.xlabel("Date")
plt.ylabel("Volume")
plt.grid(True)
plt.show()

# -----------------------------
# Moving Averages
# -----------------------------
plt.figure(figsize=(12, 5))
plt.plot(df.index, df["Close"], label="Close")
plt.plot(df.index, df["MA_5"], label="MA 5")
plt.plot(df.index, df["MA_20"], label="MA 20")
plt.title("Moving Averages")
plt.xlabel("Date")
plt.ylabel("Price")
plt.legend()
plt.grid(True)
plt.show()

# -----------------------------
# Daily Return
# -----------------------------
plt.figure(figsize=(12, 5))
plt.plot(df.index, df["Daily_Return"])
plt.title("Daily Return")
plt.xlabel("Date")
plt.ylabel("Return")
plt.grid(True)
plt.show()

# -----------------------------
# Volatility
# -----------------------------
plt.figure(figsize=(12, 5))
plt.plot(df.index, df["Volatility"])
plt.title("Volatility")
plt.xlabel("Date")
plt.ylabel("Volatility")
plt.grid(True)
plt.show()

# -----------------------------
# Correlation Matrix
# -----------------------------
print("\nCorrelation Matrix:")
print(df.corr(numeric_only=True))