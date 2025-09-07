# voice.py
import pyttsx3
import time

engine = pyttsx3.init('sapi5')

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)   # David (male, US)
engine.setProperty('rate', 170)

def speak(text):
    print(f"Jarvis 🟢: {text}")
    engine.say(text)
    engine.runAndWait()
    time.sleep(0.5)
