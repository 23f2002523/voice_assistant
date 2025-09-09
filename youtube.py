
import webbrowser
import pywhatkit
from voice import speak

def open_youtube():
    speak("Opening YouTube")
    webbrowser.open("https://www.youtube.com")


def play_song_on_youtube(song_name):
    """Play a specific song on YouTube using pywhatkit"""
    try:
        speak(f"Searching and playing {song_name} on YouTube")
        # pywhatkit automatically searches and plays the song
        pywhatkit.playonyt(song_name)
        speak(f"Playing {song_name}")
    except Exception as e:
        speak("Sorry, I couldn't play the song. Please try again.")
        print(f"Error: {e}")
