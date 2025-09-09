# main.py (UPDATED WITH WHATSAPP FUNCTIONALITY)
print("🚀 main.py started")

import speech_recognition as sr
from startup import startup_jarvis
from youtube import open_youtube, play_song_on_youtube
from whatsapp import send_whatsapp_message, open_whatsapp
from voice import speak

def listen_command():
    r = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            print("🎙️ Listening...")
            r.adjust_for_ambient_noise(source, duration=1)
            audio = r.listen(source, timeout=5, phrase_time_limit=7)

        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(f"👉 You said: {query}")
        return query.lower()
    
    except sr.UnknownValueError:
        speak("Sorry, I didn't catch that. Please say again.")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None

def extract_song_name(command):
    """Extract song name from voice command"""
    words_to_remove = ["jarvis", "play", "song", "on", "youtube"]
    
    for word in words_to_remove:
        command = command.replace(word, "")
    
    return command.strip()

if __name__ == "__main__":
    if startup_jarvis():
        speak("Jarvis is now online. I can play songs, send WhatsApp messages, and more!")
        
        while True:
            command = listen_command()
            
            if command:
                # YouTube functionality
                if "open youtube" in command and "play" not in command:
                    open_youtube()
                
                elif "play" in command and ("youtube" in command or "song" in command):
                    song_name = extract_song_name(command)
                    if song_name:
                        play_song_on_youtube(song_name)
                    else:
                        speak("Please tell me which song you want to play")
                
                # WhatsApp functionality
                elif "whatsapp" in command and "send" not in command:
                    open_whatsapp()
                
                elif "send whatsapp" in command or "whatsapp message" in command or "send message" in command:
                    send_whatsapp_message()
                
                # Exit commands
                elif "exit" in command or "stop" in command:
                    speak("Okay, shutting down. Bye boss!")
                    break
                
                else:
                    speak("I can play songs on YouTube, send WhatsApp messages, or open applications. What would you like me to do?")
