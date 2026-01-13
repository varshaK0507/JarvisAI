import pyjokes
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
from mygui import test
import threading
import subprocess
import openai
import time


# Set up OpenAI API key
openai.api_key = "INSERT KEY"
my_thread = threading.Thread(target=test)

# Start the thread
my_thread.start()

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()


talk("Hey, I'm steve")
talk("What do you need help with?")

def take_command():
    try:
        with sr.Microphone() as source:
            print("I am Listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'steve' in command:
                command = command.replace('steve', '')

    except:
        pass
    return command


def run_steve():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)

    elif 'time' in command:
        current_time = datetime.datetime.now().strftime('%I:%M %p')
        print(current_time)
        talk('current time is ' + current_time)

    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 2)
        print(info)
        talk(info)

    elif 'joke' in command:
        joke = pyjokes.get_joke()
        print(joke)
        talk(joke)

    elif 'bye' in command:
        subprocess.run(['taskkill', '/F', '/IM', 'python.exe', '/T'])
        exit()

    else:
        # User input doesn't match any predefined command, so send it to ChatGPT
        talk("Let me think about that.")

        # Send user input to ChatGPT
        response = openai.Completion.create(
            engine="text-davinci-003",  # or any other available engine
            prompt=command,
            max_tokens=100
        )

        # Get and print ChatGPT's response
        chatgpt_response = response.choices[0].text.strip()
        print("Response:", chatgpt_response)

        # Speak the ChatGPT response
        talk(chatgpt_response)


while True:
    run_steve()
    time.sleep(10)

