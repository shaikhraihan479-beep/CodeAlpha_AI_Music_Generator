import pickle
import numpy as np

# Load the processed training data
with open("../dataset/training_data.pkl", "rb") as file:
    network_input, network_output, note_to_int = pickle.load(file)

# Convert the data into NumPy arrays
X = np.array(network_input)
y = np.array(network_output)

print("Training data loaded successfully.")
print("Input shape:", X.shape)
print("Output shape:", y.shape)
print("Number of musical events:", len(note_to_int))

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Input, Embedding, LSTM, Dropout, Dense

vocab_size = len(note_to_int)

model = Sequential([
    Input(shape=(100,)),
    Embedding(vocab_size, 128),
    LSTM(256),
    Dropout(0.3),
    Dense(vocab_size, activation="softmax")
])

model.compile(
    loss="sparse_categorical_crossentropy",
    optimizer="adam"
)

model.summary()

print("Starting training...")

model.fit(
    X,
    y,
    epochs=1,
    batch_size=64
)

print("Training completed.")

model.save("../models/music_generator.keras")

print("Model saved successfully.")