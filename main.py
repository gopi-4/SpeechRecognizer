import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import sys

name = 'alexa'
listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    print(text)
    engine.say(text)
    engine.runAndWait()


# def take_command():
#     try:
#         with sr.Microphone as source:
#             print('listening...')
#             voice = listener.listen(source, None, 10)
#             command = listener.recognize_google(voice)
#             command = command.lower()
#             if 'alexa' in command:
#                 print(command)
#                 command = command.replace('alexa', '')
#     except:
#         pass
#     return command


def run_alexa():
    try:
        with sr.Microphone(None, None, 1024) as source:
            print('listening...')
            voice = listener.listen(source, None, 10)
            command = ''
            command = listener.recognize_google(voice)
            command = command.lower()
            # if name in command:
            #     command = command.replace('alexa', '')
            #     print(command)
        # talk('speak loudly')

        # print(command)
    except:
        pass

    if name in command:
        command = command.replace('alexa', '')
        print(command)
        if 'play' in command:
            song = command.replace('play', '')
            talk('playing ' + song)
            pywhatkit.playonyt(song)
        elif 'time' in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            talk('Current time is ' + time)
        elif 'wikipedia' in command:
            person = command.replace('wikipedia', '')
            info = wikipedia.summary(person, 1)
            talk(info)
        elif 'date' in command:
            talk('sorry, I have a headache')
        elif 'are you single' in command:
            talk('I am in a relationship with wifi')
        elif 'joke' in command:
            talk(pyjokes.get_joke())
        elif 'your' and 'name' in command:
            talk('are you drunk')
        elif 'marry me' in command:
            talk('sorry we are just friends')
        elif 'terminate' in command:
            talk('terminating the program')
            sys.exit()
        elif 'thank you' in command:
            talk("don't be thankful i am made for it")
        else:
            talk('This command is not recognized by my system')
        talk('what else i do for you')
    elif command == '':
        talk('please say something')
    elif 'your name' in command:
        talk('ohh my name is '+name)
        talk('what else i do for you')
    else:
        print(command)
        talk("probably you don't love me now")


talk('Please say something')

while True:
    try:
        run_alexa()
    except:
        if UnboundLocalError:
            print('Program terminated externally')
            sys.exit()
