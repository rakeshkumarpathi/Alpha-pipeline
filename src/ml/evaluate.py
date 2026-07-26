import os
import joblib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from tensorflow.keras.models import load_model
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    mean_absolute_percentage_error,
    r2_score
)

# ==========================================
# Load Data
# ==========================================

X_test = np.load("data/ml/X_test.npy")
y_test = np.load("data/ml/y_test.npy")

# ==========================================
# Load Model & Scaler
# ==========================================

model = load_model("models/lstm_model.keras")
scaler = joblib.load("models/scaler.pkl")

# ==========================================
# Predict (scaled)
# ==========================================

pred_scaled = model.predict(X_test, verbose=0).flatten()

# ==========================================
# Convert back to original stock prices
# ==========================================

features = [
    "Open","High","Low","Close","Volume",
    "Daily_Return","MA_5","MA_20","Volatility",
    "EMA_10","EMA_20","EMA_50",
    "RSI_14","MACD","MACD_Signal","MACD_Hist",
    "BB_Upper","BB_Middle","BB_Lower"
]

close_index = features.index("Close")

dummy_pred = np.zeros((len(pred_scaled), len(features)))
dummy_true = np.zeros((len(y_test), len(features)))

dummy_pred[:, close_index] = pred_scaled
dummy_true[:, close_index] = y_test

pred = scaler.inverse_transform(dummy_pred)[:, close_index]
actual = scaler.inverse_transform(dummy_true)[:, close_index]

# ==========================================
# Metrics
# ==========================================

mae = mean_absolute_error(actual, pred)
rmse = np.sqrt(mean_squared_error(actual, pred))
mape = mean_absolute_percentage_error(actual, pred) * 100
r2 = r2_score(actual, pred)

# ==========================================
# Directional Accuracy
# ==========================================

actual_direction = np.diff(actual) > 0
pred_direction = np.diff(pred) > 0

directional_accuracy = (
    np.mean(actual_direction == pred_direction) * 100
)

# ==========================================
# Naive Baseline
# ==========================================

baseline_pred = actual[:-1]
baseline_actual = actual[1:]

baseline_rmse = np.sqrt(
    mean_squared_error(
        baseline_actual,
        baseline_pred
    )
)

# ==========================================
# Print
# ==========================================

print("\n================ MODEL EVALUATION ================\n")

print(f"MAE                  : ${mae:.2f}")
print(f"RMSE                 : ${rmse:.2f}")
print(f"MAPE                 : {mape:.2f}%")
print(f"R² Score             : {r2:.4f}")
print(f"Directional Accuracy : {directional_accuracy:.2f}%")
print(f"Baseline RMSE        : ${baseline_rmse:.2f}")

print("\n==================================================")

# ==========================================
# Plot
# ==========================================

plt.figure(figsize=(15,6))

plt.plot(actual, label="Actual", linewidth=2)
plt.plot(pred, label="Predicted", linewidth=2)

plt.title("Actual vs Predicted Closing Price")

plt.xlabel("Trading Days")
plt.ylabel("Close Price")

plt.grid(True)
plt.legend()

os.makedirs("reports", exist_ok=True)

plt.savefig(
    "reports/actual_vs_predicted_real_price.png",
    dpi=300
)

plt.show()