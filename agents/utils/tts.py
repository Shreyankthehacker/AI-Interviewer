from gtts import gTTS
import os
from states import State

def audio(text,state:State):
    tts = gTTS(text, lang='en')
    tts.save("question"+str(state.count)+".mp3")
