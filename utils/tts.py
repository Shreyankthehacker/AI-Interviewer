from gtts import gTTS
import os

tts = gTTS("Hello, this is gTTS!", lang='en')
tts.save("output.mp3")

def audio(text):
    tts = gTTS(text, lang='en')
    tts.save("output.mp3")
 