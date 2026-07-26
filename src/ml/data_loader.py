import pandas as pd

# Path to the Gold layer dataset
file_path = "data/gold/AAPL_features.parquet"

# Load dataset
df = pd.read_parquet(file_path)

# Display first few rows
print("\nFirst 5 Rows")
print(df.head())

# Dataset shape
print("\nDataset Shape")
print(df.shape)

# Column names
print("\nColumns")
print(df.columns.tolist())

# Data types
print("\nData Types")
print(df.dtypes)

# Missing values
print("\nMissing Values")
print(df.isnull().sum())

# Duplicate rows
print("\nDuplicate Rows")
print(df.duplicated().sum())

# Statistical summary
print("\nSummary Statistics")
print(df.describe())