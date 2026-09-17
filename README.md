# AI Music Generator 🎵

An AI-based music generation project built using Python, TensorFlow, LSTM neural networks, and the music21 library.

The project learns musical patterns from MIDI files and generates new musical sequences using a trained LSTM model. The generated sequences are converted back into MIDI format for playback.

## Features

- Uses MIDI music data for training.
- Extracts musical notes and chords using music21.
- Converts musical events into numerical sequences.
- Uses an LSTM neural network to learn musical patterns.
- Generates new musical sequences using the trained model.
- Uses probability-based sampling for more varied music generation.
- Converts generated sequences back into MIDI format.
- Generated music can be played using any compatible MIDI player.

## Technologies Used

- Python
- TensorFlow
- Keras
- LSTM (Long Short-Term Memory)
- NumPy
- music21
- MIDI
- Git & GitHub

## Dataset

This project uses the **MAESTRO v3.0.0 MIDI dataset** provided by Google Magenta.

The dataset contains classical piano performances in MIDI format.

Dataset source:

https://magenta.tensorflow.org/datasets/maestro

### Dataset License

The MAESTRO dataset is released under the **Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0)** license.

The raw MIDI files are not uploaded to this GitHub repository because of their size and to keep the repository lightweight.

Only the dataset metadata and license information are included in the repository.

## Project Structure

    AI_Music_Generator/
    │
    ├── Dataset/
    │   └── maestro-v3.0.0/
    │       ├── LICENSE
    │       ├── README
    │       ├── maestro-v3.0.0.csv
    │       └── maestro-v3.0.0.json
    │
    ├── models/
    │   └── music_generator.keras
    │
    ├── output/
    │   └── generated_music.mid
    │
    ├── src/
    │   ├── preprocess.py
    │   ├── train.py
    │   └── generate.py
    │
    ├── .gitignore
    ├── README.md
    └── requirements.txt

Note: The trained model, generated MIDI file, processed data, virtual environment, and raw MIDI files are kept locally and are excluded from GitHub to keep the repository lightweight.

## How the Project Works

The project is divided into three main stages:

### 1. Data Preprocessing

The `preprocess.py` script searches the MAESTRO dataset for MIDI files.

It extracts:

- Individual musical notes
- Chords
- Musical event sequences

These musical events are converted into numerical values so that they can be processed by the neural network.

The script then creates sequences of 100 musical events.

The first 100 events are used as input and the next musical event is used as the target output.

### 2. Model Training

The `train.py` script loads the processed training data and trains an LSTM neural network.

The model contains:

- Embedding layer
- LSTM layer
- Dropout layer
- Dense output layer

The LSTM learns relationships between previous musical events and predicts the next musical event.

After training, the model is saved as:

    models/music_generator.keras

### 3. Music Generation

The `generate.py` script loads the trained model and processed data.

It starts with an initial musical sequence and repeatedly predicts the next musical event.

Probability-based sampling is used instead of always selecting the most probable event. This helps create more varied musical sequences.

The generated notes and chords are then converted into a MIDI file.

The generated file is saved as:

    output/generated_music.mid

## Installation

Make sure Python 3.11 is installed.

Create a virtual environment:

    python -m venv venv

Activate the virtual environment on Windows:

    venv\Scripts\activate

Install the required libraries:

    pip install -r requirements.txt

## Running the Project

### Step 1: Preprocess the Dataset

Go to the `src` folder:

    cd src

Run:

    python preprocess.py

This extracts musical events from the MIDI files and creates the processed training data.

### Step 2: Train the Model

Run:

    python train.py

The model will be trained and saved inside the `models` folder.

### Step 3: Generate Music

Run:

    python generate.py

The generated MIDI file will be saved inside the `output` folder.

## Model Architecture

The project uses the following neural network architecture:

    Input
      ↓
    Embedding Layer
      ↓
    LSTM Layer
      ↓
    Dropout Layer
      ↓
    Dense Layer
      ↓
    Musical Event Prediction

### Embedding Layer

The Embedding layer converts numerical musical event IDs into dense vector representations that the neural network can learn from.

Embedding size used:

    128

### LSTM Layer

The LSTM layer learns patterns and relationships between musical events over a sequence.

LSTM units:

    256

### Dropout Layer

A dropout rate of:

    0.3

is used to reduce overfitting during training.

### Dense Layer

The final Dense layer predicts the probability of the next musical event.

The output size depends on the number of unique musical events found in the dataset.

## Training Details

The project found:

- MIDI files available: 1,276
- MIDI files used for current training: 50
- Unique musical events: 37,168
- Training sequences: 149,903
- Sequence length: 100
- Epochs: 1
- Batch size: 32
- Training hardware: CPU
- Framework: TensorFlow/Keras

The trained model contains approximately:

    14.7 million parameters

The current training configuration was kept relatively small in terms of dataset usage and epochs so that the project could be trained on a normal laptop CPU.

## Output

The generated music is saved in MIDI format:

    output/generated_music.mid

The MIDI file can be opened using a MIDI-compatible music player or digital audio workstation.

## Limitations

- Only 50 MIDI files are currently used for training even though the dataset contains 1,276 MIDI files.
- The model is trained for only 1 epoch.
- Training is performed on CPU.
- The generated music may not always have strong musical structure.
- The project focuses on generating MIDI sequences rather than high-quality audio.
- Longer training and more data could improve the learned musical patterns.

## Future Improvements

The project can be improved by:

- Training on more MIDI files.
- Increasing the number of training epochs.
- Using a GPU for faster training.
- Improving the music generation algorithm.
- Adding temperature-based sampling for better control over randomness.
- Improving rhythm and note-duration handling.
- Training on larger and more diverse music datasets.
- Using more advanced architectures such as Transformers.
- Creating a graphical user interface for easier music generation.
- Converting generated MIDI files into audio formats.

## Conclusion

This project demonstrates how Artificial Intelligence and Deep Learning can be used for music generation.

The LSTM model learns patterns from sequences of musical notes and chords and uses those learned patterns to generate new musical sequences.

The generated sequences are converted into MIDI format, allowing the resulting music to be played and evaluated.

The project provides practical experience with:

- Python
- Data preprocessing
- MIDI processing
- Neural networks
- LSTM
- TensorFlow/Keras
- AI-based content generation
- Git and GitHub

## Internship Information

**Organization:** CodeAlpha

**Internship Domain:** Artificial Intelligence

**Project:** Music Generation with AI

**Task:** Task 3 - Music Generation with AI

## Acknowledgement

This project was developed as part of the **CodeAlpha Artificial Intelligence Internship**.

Special thanks to CodeAlpha for providing the opportunity to work on an Artificial Intelligence project involving music generation and deep learning.

The MAESTRO dataset used in this project is provided by Google Magenta.