import sounddevice as sd
import numpy as np
import webrtcvad
import wave
import time

# Parameters
FORMAT = np.int16  # Format of the audio data
CHANNELS = 1  # Mono channel
RATE = 16000  # Sample rate (16kHz)
CHUNK_SIZE = 1024  # Size of the audio chunks to process at a time
VAD_MODE = 3  

# Initialize WebRTC VAD
vad = webrtcvad.Vad(VAD_MODE)

# Function to check if the frame contains speech
def is_speech(frame):
    try:
        return vad.is_speech(frame, RATE)
    except Exception as e:
        print(f"Error processing frame: {e}")
        return False

# Record audio in chunks from sounddevice
def record_audio(duration=10, filename="output.wav"):
    frames = []
    with sd.InputStream(samplerate=RATE, channels=CHANNELS, dtype=FORMAT) as stream:
        print("Recording... Speak now!")
        start_time = time.time()
        recording = False

        while time.time() - start_time < duration:
            audio_chunk = stream.read(CHUNK_SIZE)[0]  # Read audio chunk
            audio_chunk = np.frombuffer(audio_chunk, dtype=np.int16)

            # Check if there is speech in the audio chunk using VAD
            if len(audio_chunk) == CHUNK_SIZE:  # Ensure we have enough data to process
                if is_speech(audio_chunk):
                    if not recording:
                        print("Speech detected, starting recording...")
                        recording = True
                    frames.append(audio_chunk)
                elif recording:
                    # Stop recording if silence is detected after speech
                    print("Silence detected, stopping recording...")
                    break
            else:
                print(f"Skipping chunk of invalid size: {len(audio_chunk)}")

        if frames:
            print(f"Saving the recording as {filename}...")
            # Save the recorded frames as a WAV file
            with wave.open(filename, 'wb') as wf:
                wf.setnchannels(CHANNELS)
                wf.setsampwidth(np.dtype(FORMAT).itemsize)
                wf.setframerate(RATE)
                wf.writeframes(b''.join(frames))
            print(f"Recording saved as {filename}")

# Example usage: Record for 10 seconds and save the audio to "output.wav"
record_audio(duration=10, filename="output.wav")
