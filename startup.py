import pyttsx3
import speech_recognition as sr  # future me use hoga

# Text to Speech function
def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

# Unlock function
def voice_unlock(secret_password="northstar"):
    speak("Jarvis activated. Please enter your password to unlock Jarvis.")
    attempts = 0

    while attempts < 3:
        user_input = input("Enter your password: ")

        if user_input.lower() == secret_password.lower():
            speak("Hi, I am Jarvis. Nice to meet you again.")
            return True
        else:
            attempts += 1
            if attempts < 3:
                speak("Wrong password. Try again.")
            else:
                speak("Wrong password. Jarvis locked.")
                return False
