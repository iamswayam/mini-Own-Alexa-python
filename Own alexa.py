import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import googlesearch
import pyjokes


listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)
            else:
                talk('with whom you are talking to. By the way, I am alexa')
    except:
        pass
    return command


def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'date' in command:
        date = datetime.datetime.now().strftime('%b %d')
        talk('Today is ' + date)
    elif 'love you' in command:
        talk('That is sweet of you but I would die single rather fall in love with you')
    elif 'who the heck is' in command:
        person = command.replace('who the heck is', '')
        info = wikipedia.summary(person, 2)
        talk(info)
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'nothing' in command:
        exit
    else:
        talk('Sorry, I could not understand. come again')


while True:
    run_alexa()
