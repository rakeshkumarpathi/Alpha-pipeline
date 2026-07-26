import os
import joblib
import numpy as np
import pandas as pd

from sklearn.preprocessing import MinMaxScaler

# ==========================================
# Load Dataset
# ==========================================

df = pd.read_parquet("data/ml/AAPL_ml.parquet")

print("Dataset Shape :", df.shape)

# ==========================================
# Feature Columns
# ==========================================

features = [
    "Open",
    "High",
    "Low",
    "Close",
    "Volume",
    "Daily_Return",
    "MA_5",
    "MA_20",
    "Volatility",
    "EMA_10",
    "EMA_20",
    "EMA_50",
    "RSI_14",
    "MACD",
    "MACD_Signal",
    "MACD_Hist",
    "BB_Upper",
    "BB_Middle",
    "BB_Lower"
]

target = "Close"

# ==========================================
# Scale Features
# ==========================================

scaler = MinMaxScaler()

scaled_data = scaler.fit_transform(df[features])

# Create models folder if missing
os.makedirs("models", exist_ok=True)

joblib.dump(scaler, "models/scaler.pkl")

print("Scaler saved successfully.")

# ==========================================
# Create Sequences
# ==========================================

sequence_length = 60

X = []
y = []

target_index = features.index(target)

for i in range(sequence_length, len(scaled_data)):
    X.append(scaled_data[i-sequence_length:i])
    y.append(scaled_data[i][target_index])

X = np.array(X)
y = np.array(y)

print("\nSequence Shape")
print("X :", X.shape)
print("y :", y.shape)

# ==========================================
# Train/Test Split
# ==========================================

split = int(len(X) * 0.8)

X_train = X[:split]
X_test = X[split:]

y_train = y[:split]
y_test = y[split:]

print("\nTraining Data :", X_train.shape)
print("Testing Data  :", X_test.shape)

# ==========================================
# Save Arrays
# ==========================================

os.makedirs("data/ml", exist_ok=True)

np.save("data/ml/X_train.npy", X_train)
np.save("data/ml/X_test.npy", X_test)

np.save("data/ml/y_train.npy", y_train)
np.save("data/ml/y_test.npy", y_test)

print("\nPreprocessing Completed Successfully.")