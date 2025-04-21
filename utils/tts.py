from gtts import gTTS
import os

tts = gTTS("What is machine learning ", lang='en')
tts.save("question.mp3")

def audio(text):
    tts = gTTS(text, lang='en')
    tts.save("question.mp3")
