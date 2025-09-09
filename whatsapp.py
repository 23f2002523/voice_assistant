import webbrowser
import pywhatkit
import time 

from voice import speak
from datetime import datetime,timedelta
import speech_recognition as sr


def listen_for_input(prompt_message):
    """Listen for user voice input"""
    speak(prompt_message)

    r = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            print("🎙️ Listening for response...")
            r.adjust_for_ambient_noise(source, duration=1)  # noise handle karega
            audio = r.listen(source, timeout=10, phrase_time_limit=7)

        print("Recognizing...")
        response = r.recognize_google(audio, language="en-in")
        print(f"👉 You said: {response}")
        return response.lower().strip()
    
    except sr.UnknownValueError:
        speak("Sorry, I didn't catch that. Please say again.")
        return None
    except sr.RequestError:
        speak("Sorry, speech recognition service is not available.")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None
    



def get_contact_number(contact_name):
    """Convert contact name to phone number or validate phone number"""
    # Check if it's already a phone number
    if contact_name.replace("+", "").replace(" ", "").replace("-", "").isdigit():
        # It's already a phone number
        if not contact_name.startswith("+"):
            speak("Please include the country code. For India, it should start with +91")
            return None
        return contact_name
    
    # It's a contact name, ask for phone number
    speak(f"I need the phone number for {contact_name}. Please say the number with country code.")
    
    for attempt in range(3):
        number = listen_for_input("Please say the phone number")
        if number:
            # Try to extract numbers from speech
            digits = ''.join(filter(str.isdigit, number))
            if len(digits) >= 10:
                # Assume it's an Indian number if no country code
                if len(digits) == 10:
                    formatted_number = f"+91{digits}"
                else:
                    formatted_number = f"+{digits}"
                
                speak(f"Should I send to {formatted_number}?")
                confirmation = listen_for_input("Say yes or no")
                if confirmation and "yes" in confirmation:
                    return formatted_number
        
        speak("Please try again")
    return None



def collect_message_content():
    """Collect message content from user voice input"""
    speak("What message would you like to send? Start speaking after the beep.")
    
    message_parts = []
    
    while True:
        message_part = listen_for_input("Say your message, or say 'message completed' when done")
        
        if message_part:
            if "message completed" in message_part or "completed" in message_part:
                break
            elif "stop" in message_part or "cancel" in message_part:
                return None
            else:
                # Remove command words from the message
                clean_message = message_part.replace("message", "").strip()
                if clean_message:
                    message_parts.append(clean_message)
                    speak("Got it. Continue speaking or say 'message completed'")
        else:
            speak("I didn't hear anything. Please try again.")
    
    if message_parts:
        full_message = " ".join(message_parts)
        speak(f"Your complete message is: {full_message}")
        
        # Confirm message
        confirmation = listen_for_input("Should I send this message? Say yes or no")
        if confirmation and "yes" in confirmation:
            return full_message
        else:
            speak("Message cancelled")
            return None
    
    speak("No message content received")
    return None


    
    
def send_whatsapp_message():
    """Complete WhatsApp messaging workflow with voice interaction"""
    try:
        speak("Let's send a WhatsApp message!")
        
        # Step 1: Get contact information
        speak("Whom would you like to send the message to?")
        contact_input = listen_for_input("Say the contact name or phone number")
        
        if not contact_input:
            speak("No contact information received. Cancelled.")
            return
        
        # Step 2: Get phone number
        phone_number = get_contact_number(contact_input)
        if not phone_number:
            speak("Could not get valid phone number. Cancelled.")
            return
        
        # Step 3: Collect message content
        message_content = collect_message_content()
        if not message_content:
            speak("No message to send. Cancelled.")
            return
        
        # Step 4: Send the message
        speak("Sending your WhatsApp message now...")
        
        try:
            # Try instant send first
            pywhatkit.sendwhatmsg_instantly(phone_number, message_content, wait_time=15, tab_close=True)
            speak("Message sent successfully!")
            
        except Exception as e:
            # Fallback to scheduled message (1 minute from now)
            current_time = datetime.now() + timedelta(minutes=1)
            hour = current_time.hour
            minute = current_time.minute
            
            speak(f"Scheduling message for {hour}:{minute:02d}")
            pywhatkit.sendwhatmsg(phone_number, message_content, hour, minute)
            speak("Message scheduled and will be sent shortly!")
            
    except Exception as e:
        speak("Sorry, I encountered an error while sending the message")
        print(f"Error: {e}")




CONTACTS = {
    "Panda IITM": "+917990590921",
    "dad": "+919876543211",
    "brother": "+919876543212",
    "rohan": "+919812345678"
}

def get_contact_number(contact_name):
    contact_name = contact_name.lower()
    num = CONTACTS.get(contact_name)
    if num:
        return num
    else:
        speak(f"I couldn't find {contact_name} in your contact list.")
        return None

def send_whatsapp_message():
    speak("Whom would you like to send the message to?")
    contact_input = listen_for_input("Say the contact name")
    if not contact_input:
        speak("No contact name received. Cancelled.")
        return
    phone_number = get_contact_number(contact_input.strip())
    if not phone_number:
        return
    
    speak("What message would you like to send?")
    message = listen_for_input("Say your message, then say 'message completed' when finished")
    if not message or "message completed" in message:
        speak("No message to send. Cancelled.")
        return

    speak("Sending your WhatsApp message now...")
    try:
        pywhatkit.sendwhatmsg_instantly(phone_number, message, wait_time=15, tab_close=True)
        speak("Message sent successfully!")
    except Exception as e:
        speak("Sorry, I couldn't send your message.")
        print(f"Error: {e}")



def open_whatsapp():
    """Open WhatsApp Web"""
    speak("Opening WhatsApp Web")
    webbrowser.open("https://web.whatsapp.com")