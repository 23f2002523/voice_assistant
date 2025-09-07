# main.py
print("🚀 main.py started")

import speech_recognition as sr
from startup import startup_jarvis
from youtube import open_youtube
from voice import speak

def listen_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎙️ Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(f"👉 You said: {query}")
        return query.lower()
    except:
        speak("Sorry, I didn't catch that. Please say again.")
        return None


if __name__ == "__main__":
    if startup_jarvis():
        speak("Jarvis is now online. Waiting for your command.")

        while True:
            command = listen_command()

            if command:
                if "open youtube" in command:
                    open_youtube()

                elif "exit" in command or "stop" in command:
                    speak("Okay, shutting down. Bye boss!")
                    break
