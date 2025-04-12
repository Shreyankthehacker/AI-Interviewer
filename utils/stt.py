import whisper
import warnings
warnings.filterwarnings("ignore")

model = whisper.load_model("tiny")  


import sounddevice as sd
from scipy.io.wavfile import write

def record_audio(filename="input.wav", duration=5, fs=44100):
    """
    Records audio from the microphone and saves it to a WAV file.
    
    :param filename: Output filename (WAV)
    :param duration: Duration of recording in seconds
    :param fs: Sample rate (Hz)
    """
    print(f"Recording for {duration} seconds...")
    audio_data = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='int16')
    sd.wait()  
    write(filename, fs, audio_data)
    print(f"Recording saved to {filename}")


def transcribe(audio):
    return model.transcribe(audio)['text']

print(transcribe("output.mp3"))


