import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()

# voices = engine.getProperty('voices')
# engine.setProperty('voice', voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print('listining.......')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'VA' in command:
                command = command.replace('hey', '')
                print(command)
    except:
        pass
    return command

def run_VA():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('Playing' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%H:%M %p')
        print(time)
        talk('Current time is ' + time)
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'date' in command:
        answer = 'What about your Girlfriend'
        print(answer)
        talk('What about your Girlfriend')
    elif 'single' in command:
        talk('I am with relationship with google')
    elif 'jokes' in command:
        talk(pyjokes.get_joke())
    elif 'how are you' in command:
        talk('I am good what about you ')
    else:
        talk('Please say it again ')


while(True):
    run_VA()
