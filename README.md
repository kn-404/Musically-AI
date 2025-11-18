# Musically-AI
Developed a Python pipeline using music21, mido, note_seq, and Magenta to analyze and generate melodies from keyboard MIDI data. Automated melody creation with neural RNNs (basic_RNN.mag) and visualized note frequency patterns using matplotlib. Explored how machine learning models produce musically coherent MIDI outputs.

# Technologies Used
1. Magenta (Melody-RNN) — AI model for melody generation
2. note_seq — MIDI to NoteSequence conversion
3. pretty_midi — Pitch -> note and pitch -> frequency utilities
4. matplotlib — Visualization of musical data
5. subprocess & standard Python libraries — Running CLI generation and file handling

# How it works
1. User provides:
   - Location of midi file
   - Location of a Magenta .mag model bundle file (basic_rnn.mag used in testing)
2. The Melody-RNN model generates a 64-step continuation of the original piece.
3. The script prints the notes in both files.
4. A graph is created to show the frequencies of the generated notes.

# Instructions:
Prerequisites: Python 3.7, Ubuntu (tested on Ubuntu 24.04.1 LTS), Windows Subsystem for Linux (WSL) required (code runs inside WSL, not native Windows)
Required Python packages: music21, mido, note_seq, matplotlib, pretty_midi

1. Setup Magenta/Tensorflow on your system (follow this guide: http://bit.ly/4pex6em)
2. Install the required dependencies
3. Run the Python script
4. Enter the path to a primer MIDI file and a model bundle (.mag) when prompted
5. Output MIDI and a plotted visualization are stored in gen_out/ and saved as an image file (output_plot.png)

# Expect Output (Example):
![Graph](https://github.com/user-attachments/assets/0968502b-35e5-45be-b5cd-2430bd6fe3de)

# Challenges:
Mainly getting the code to function. Installing magenta and creating a wsl subsystem was a huge pain, then figuring out how to use it and get it to generate took several weeks. But overall, this project was really fun and I do plan on creating more AI based projects in the future, to really harness the power of Machine Learning

# License MIT © kn 404
