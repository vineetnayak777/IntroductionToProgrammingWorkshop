import pyttsx3  # pip install pyttsx3
import speech_recognition as sr  # pip install speechRecognition
import datetime
import wikipedia  # pip install wikipedia
import webbrowser
import os
import smtplib

chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning!")

    elif 12 <= hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am your personal assistant. Please tell me how may I help you")


def takeCommand():
    # It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception:
        # print(e)
        print("Say that again please...")
        return "None"
    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()


if __name__ == "__main__":
    wishMe()
    while True:
        # if 1:
        query = takeCommand().lower()
        print(query)

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.get(chrome_path).open("youtube.com")

        elif 'open google' in query:
            webbrowser.get(chrome_path).open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.get(chrome_path).open("stackoverflow.com")

        elif 'search' in query:
            query = query.replace("search", "")
            query = query.replace("for", "")
            query = query.replace("best", "")
            query = query.replace("courses", "")
            query = query.replace("course", "")

            webbrowser.get(chrome_path).open("edvicer.com/courses?q=" + query)

        elif 'play music' in query:
            music_dir = 'path to music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Mam, the time is {strTime}")

        elif 'email send' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "receiver@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend . I am not able to send this email")
