# assistant.py

import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import webbrowser
import pyjokes

engine = pyttsx3.init()

def talk(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()

def take_command():
    listener = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            print("Listening...")
            audio = listener.listen(source)
            command = listener.recognize_google(audio).lower()
            print("You said:", command)
            return command
    except:
        talk("Sorry, I couldn't hear.")
        return ""

def run_assistant():
    command = take_command()

    if "play" in command:
        song = command.replace("play", "")
        talk(f"Playing {song}")
        pywhatkit.playonyt(song)

    elif "time" in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk(f"The time is {time}")

    elif "google" in command:
        webbrowser.open("https://www.google.com")
        talk("Opening Google")

    elif "joke" in command:
        talk(pyjokes.get_joke())

    elif "stop" in command or "exit" in command:
        talk("Goodbye")
        exit()

    else:
        talk("I didn't understand that.")
