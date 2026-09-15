import pickle
import numpy as np
from tensorflow.keras.models import load_model
from music21 import stream, note, chord

# Load the trained model
model = load_model("../models/music_generator.keras")

# Load the processed data
with open("../dataset/training_data.pkl", "rb") as file:
    network_input, network_output, note_to_int = pickle.load(file)

# Create the reverse mapping: number → musical event
int_to_note = {number: note for note, number in note_to_int.items()}

print("Model and data loaded successfully.")

sequence_length = 100
generation_length = 200

# Use the first training sequence as our starting point
start_sequence = network_input[0]

pattern = list(start_sequence)

generated_notes = []

for _ in range(generation_length):
    input_sequence = np.array(pattern[-sequence_length:])
    input_sequence = input_sequence.reshape(1, sequence_length)

    prediction = model.predict(input_sequence, verbose=0)

    predicted_index = np.random.choice(
    len(prediction[0]),
    p=prediction[0] / np.sum(prediction[0])
)

    generated_notes.append(int_to_note[predicted_index])

    pattern.append(predicted_index)

print(f"Generated {len(generated_notes)} musical events.")

# Create a music stream
output = stream.Stream()

for item in generated_notes:
    if "." in item:
        # Convert chord string back into a chord
        pitches = item.split(".")
        output.append(chord.Chord(pitches))
    else:
        # Convert note string back into a note
        output.append(note.Note(item))

# Save the generated music
output.write("midi", fp="../output/generated_music.mid")

print("Generated MIDI file saved successfully.")