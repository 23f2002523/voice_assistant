# startup.py
from voice import speak

def startup_jarvis(secret_password="1234"):
    speak("Jarvis Activated. Please enter your password to unlock.")

    attempts = 0
    while attempts < 3:
        password = input("Enter Password: ")

        if password == secret_password:
            speak("Hi, I am Jarvis. Nice to meet you again.")
            return True
        else:
            attempts += 1
            speak("Wrong password")

    speak("Jarvis locked due to 3 failed attempts.")
    return False
