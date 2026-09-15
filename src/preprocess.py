import os
import pickle
from music21 import converter, instrument, note, chord

DATASET_PATH = "../dataset"

midi_files = []

for root, dirs, files in os.walk(DATASET_PATH):
    for file in files:
        if file.endswith(".mid") or file.endswith(".midi"):
            midi_files.append(os.path.join(root, file))

print(f"Found {len(midi_files)} MIDI files.")

notes = []

for file in midi_files[:50]:
    try:
        midi = converter.parse(file)

        for element in midi.flatten().notes:
            if isinstance(element, note.Note):
                notes.append(str(element.pitch))

            elif isinstance(element, chord.Chord):
                notes.append(
                    ".".join(str(n) for n in element.pitches)
                )

    except Exception as e:
        print(f"Skipped: {file}")

print(f"Total musical events extracted: {len(notes)}")

with open("../dataset/notes.pkl", "wb") as file:
    pickle.dump(notes, file)

print("Processed data saved successfully.")

# Create a list of unique musical events
unique_notes = sorted(set(notes))

# Create a number for each musical event
note_to_int = {note: number for number, note in enumerate(unique_notes)}

print(f"Unique musical events: {len(unique_notes)}")

sequence_length = 100

network_input = []
network_output = []

for i in range(len(notes) - sequence_length):
    sequence = notes[i:i + sequence_length]
    target = notes[i + sequence_length]

    network_input.append(
        [note_to_int[n] for n in sequence]
    )
    network_output.append(note_to_int[target])

print(f"Training sequences created: {len(network_input)}")

# Save the training data
with open("../dataset/training_data.pkl", "wb") as file:
    pickle.dump((network_input, network_output, note_to_int), file)

print("Training data saved successfully.")