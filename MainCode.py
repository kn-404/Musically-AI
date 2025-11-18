import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

import subprocess
import sys
import os
import glob

import note_seq as ns                                        
import pretty_midi                                          

def call_melody_rnn(primer_midi, bundle, output_dir):
    """Invoke the Magenta CLI to generate a melody continuation."""
    cmd = [
        "melody_rnn_generate",
        "--config=basic_rnn",                                 
        f"--bundle_file={bundle}",
        f"--output_dir={output_dir}",
        "--num_outputs=1",
        "--num_steps=64",
        f"--primer_midi={primer_midi}"
    ]
    subprocess.run(cmd, check=True)

def load_and_print(midi_path):
    """Load a MIDI via note_seq and print its note names."""
    # Convert MIDI file → NoteSequence
    seq = ns.midi_io.midi_file_to_sequence_proto(midi_path)  
    print("-> Notes in", os.path.basename(midi_path))
    for note in seq.notes:
        # Convert MIDI pitch → human name
        print(" ", pretty_midi.note_number_to_name(note.pitch))  

def plot_frequencies(midi_path):
    """Plot note index vs frequency of a generated MIDI."""
    seq = ns.midi_io.midi_file_to_sequence_proto(midi_path)
    # Map each pitch → frequency in Hz
    freqs = [pretty_midi.note_number_to_hz(n.pitch) for n in seq.notes]  
    plt.figure(figsize=(5,3))
    plt.plot(freqs, marker='o')
    plt.xlabel("Note Index")
    plt.ylabel("Frequency (Hz)")
    plt.title("Frequencies of Generated Melody")
    plt.tight_layout()
    plt.savefig("output_plot.png")


def main():
    primer = input("Path to primer MIDI file: ").strip()
    bundle = input("Path to basic_rnn.mag bundle: ").strip()
    outdir = "gen_out"
    os.makedirs(outdir, exist_ok=True)

    print("Generating with Melody RNN…")
    call_melody_rnn(primer, bundle, outdir)

    # Find the first generated MIDI file
    gen_files = glob.glob(os.path.join(outdir, "*.mid"))
    if not gen_files:
        print("No output MIDI found."); sys.exit(1)
    gen_midi = gen_files[0]

    # Print and plot
    load_and_print(primer)
    load_and_print(gen_midi)
    plot_frequencies(gen_midi)

if __name__ == "__main__":
    main()
