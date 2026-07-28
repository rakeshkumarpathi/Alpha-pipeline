import os
import joblib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from keras.models import load_model

# =====================================
# Load Model & Scaler
# =====================================

model = load_model("models/lstm_model.keras")
scaler = joblib.load("models/scaler.pkl")

# =====================================
# Load Dataset
# =====================================

df = pd.read_parquet("data/ml/AAPL_ml.parquet")

features = [
    "Open","High","Low","Close","Volume",
    "Daily_Return","MA_5","MA_20","Volatility",
    "EMA_10","EMA_20","EMA_50",
    "RSI_14","MACD","MACD_Signal","MACD_Hist",
    "BB_Upper","BB_Middle","BB_Lower"
]

scaled = scaler.transform(df[features])

sequence = scaled[-60:]

predictions = []

for _ in range(30):

    x = np.expand_dims(sequence, axis=0)

    pred = model.predict(x, verbose=0)[0][0]

    predictions.append(pred)

    new_row = sequence[-1].copy()
    new_row[3] = pred

    sequence = np.vstack([sequence[1:], new_row])

dummy = np.zeros((30, len(features)))
dummy[:,3] = predictions

future_close = scaler.inverse_transform(dummy)[:,3]

future = pd.DataFrame({
    "Day": range(1,31),
    "Predicted_Close": future_close
})

os.makedirs("data/predictions", exist_ok=True)

future.to_csv(
    "data/predictions/predictions.csv",
    index=False
)

print(future)

plt.figure(figsize=(12,5))

plt.plot(
    future["Day"],
    future["Predicted_Close"],
    marker="o"
)

plt.title("Next 30-Day Stock Forecast")

plt.xlabel("Future Day")

plt.ylabel("Predicted Close Price")

plt.grid(True)

plt.savefig("reports/future_prediction.png")

plt.show()