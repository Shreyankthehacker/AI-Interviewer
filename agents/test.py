import sounddevice as sd

def test_microphone():
    print("Testing microphone...")
    # Try recording a short sample and play it back
    duration = 5  # seconds
    sample_rate = 16000
    print("Start speaking...")

    # Record audio
    recording = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1, dtype='int16')
    sd.wait()  # Wait until the recording is done

    print("Recording finished.")
    
    # Play it back
    print("Playing back the recording...")
    sd.play(recording, sample_rate)
    sd.wait()  # Wait until playback finishes

test_microphone()
