import os
import numpy as np
import matplotlib.pyplot as plt

from keras.models import Sequential
from keras.layers import Input, LSTM, Dense, Dropout
from keras.callbacks import EarlyStopping, ModelCheckpoint, ReduceLROnPlateau

# ==========================================
# Load Data
# ==========================================

X_train = np.load("data/ml/X_train.npy")
X_test = np.load("data/ml/X_test.npy")

y_train = np.load("data/ml/y_train.npy")
y_test = np.load("data/ml/y_test.npy")

print("Training Shape :", X_train.shape)
print("Testing Shape  :", X_test.shape)

# ==========================================
# Model
# ==========================================

model = Sequential([

    Input(shape=(X_train.shape[1], X_train.shape[2])),

    LSTM(
        256,
        return_sequences=True
    ),

    Dropout(0.30),

    LSTM(
        128,
        return_sequences=True
    ),

    Dropout(0.30),

    LSTM(
        64,
        return_sequences=True
    ),

    Dropout(0.25),

    LSTM(
        32
    ),

    Dense(
        64,
        activation="relu"
    ),

    Dense(
        32,
        activation="relu"
    ),

    Dense(
        16,
        activation="relu"
    ),

    Dense(1)

])

model.compile(

    optimizer="adam",

    loss="mse",

    metrics=["mae"]

)

model.summary()

# ==========================================
# Callbacks
# ==========================================

os.makedirs("models", exist_ok=True)

checkpoint = ModelCheckpoint(

    "models/lstm_model.keras",

    monitor="val_loss",

    save_best_only=True,

    verbose=1

)

early_stop = EarlyStopping(

    monitor="val_loss",

    patience=20,

    restore_best_weights=True

)

reduce_lr = ReduceLROnPlateau(

    monitor="val_loss",

    factor=0.5,

    patience=5,

    min_lr=1e-6,

    verbose=1

)

# ==========================================
# Train
# ==========================================

history = model.fit(

    X_train,

    y_train,

    validation_data=(X_test, y_test),

    epochs=100,

    batch_size=32,

    callbacks=[

        checkpoint,

        early_stop,

        reduce_lr

    ],

    verbose=1

)

# ==========================================
# Save
# ==========================================

model.save(

    "models/final_lstm.keras"

)

print("\nTraining Completed.")

# ==========================================
# Plot
# ==========================================

plt.figure(figsize=(12,5))

plt.plot(

    history.history["loss"],

    label="Training Loss"

)

plt.plot(

    history.history["val_loss"],

    label="Validation Loss"

)

plt.xlabel("Epoch")

plt.ylabel("Loss")

plt.title("Training vs Validation Loss")

plt.legend()

plt.grid(True)

os.makedirs("reports", exist_ok=True)

plt.savefig(

    "reports/training_loss.png"

)

plt.show()