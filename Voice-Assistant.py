import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import random
import subprocess
import pyjokes
import time
import pyautogui
import psutil
import pyperclip
import ctypes
import winshell
import cv2
from googletrans import Translator
import datetime
import time
import winsound
import pyaudio

#speech to text
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id) 

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<17:
        speak("Good AfterNoon!")
    elif hour>=17 and hour<20:
        speak("Good Evening!")
    else:
        speak("Good Night")

    name =("How may I help you?")
    speak("I am your Personal Assistant.") 
    speak(name) 

def takeCommand():
    #take microphone input from user and return string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.energy_threshold = 200  
        r.pause_threshold = 0.5 
        audio = r.listen(source)

    try:
        print("Recognizing.....")
        query = r.recognize_google(audio, language='en-in')
        print(f"You said: {query}\n")

    except Exception:
        
        print('Your last  command could\'t be heard')
        speak("Say that again please!!!")
        return "None"

    return query

def date():
    year = int(datetime.datetime.now().year)
    month = datetime.datetime.now().strftime("%B")
    date = int(datetime.datetime.now().day)
    speak('Today is')
    speak(date, month, year)


if __name__== "__main__":
    # speak("Helloo..")

    wishMe()

    while True:
        query = takeCommand().lower()
        # Logic for executing tasks based on query
        if 'wikipedia' in query or 'details about' in query or 'tell me about' in query or 'who is' in query:
            speak('Searching Wikipedia....')
            query = query.replace("wikipedia", "")
            query = query.replace("details about", "")
            query = query.replace("tell me about", "")
            query = query.replace("who is", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
      
        elif 'how are you' in query or 'how are you doing' in query or 'whats up' in query:
            speak("I am fine, what about you?")
            query = takeCommand()
            if 'good' in query  or 'healthy' in query or 'fine' in query:
                speak("Nice to hear that!!!")
            if 'not fine' in query or 'not well' in query or 'not good' in query or 'feeling low' in query or 'not in mood' in query:
                speak("sad to hear that!!!")
                

        elif 'where is' in query:
            query = query.replace("where is","")      
            location = query
            speak('Just a second, showing you were is' +location)
            url = 'https://www.google.nl/maps/place/' + location + '/&amp;'
            webbrowser.get().open(url)
            
        elif 'check my internet connection' in query or 'am I connected to internet' in query:
            hostname="google.co.in"
            response=os.system("ping -c 1" +hostname)
            if response==0:
                speak("Check your Internet Connection")
            else:
                speak("You are connected to internet")

        elif 'next window' in query or 'switch back' in query or 'next' in query:
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            time.sleep(1)
            pyautogui.keyUp("alt")
            speak("window switched")

        elif 'previous window' in query or 'last window' in query or 'previous' in query:
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            time.sleep(1)
            pyautogui.keyUp("alt")
            speak("anything else?")

        elif 'date' in query:
            date()

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")

        elif 'search' in query:
            query = query.replace("search", "")
            url = f"https://www.google.com/search?q={query}"
            webbrowser.get().open(url)
            print(query)
            speak("Here is what I got form search result" + query)


        elif 'open youtube' in query:
            speak('Opening Youtube')
            webbrowser.open("https://youtube.com/")

        elif 'open gmail' in query:
            speak("Opening gmail")
            webbrowser.open('https://mail.google.com')

        elif 'recently closed tabs' in query or 'recently closed tabs' in query:
            try:
                pyautogui.keyDown("ctrl")
                pyautogui.keyDown("shift")
                pyautogui.press("T")
                pyautogui.keyUp("ctrl")
                pyautogui.keyUp("shift")
                speak("Recently closed tabs has been opened")
            except Exception as e:
                speak("No recent tabs found")

        elif 'open chrome' in query:
            try:
                speak('opening chrome')
                codepath = "chrome.exe"
                os.startfile(codepath)
            except Exception as e:
                speak("Chrome Not found")

        elif 'close chrome' in query:
            os.system("taskkill /f /im chrome.exe")
            speak('chrome has been closed')
   
        elif 'play music' in query:
            speak("Playing songs for you. Hope you like it")
            music_dir = 'Your Directory'
            songs = os.listdir(music_dir)
            rd = random.choice(songs)
            print(songs)
            for songs in songs:
                if songs.endswith('.mp3'):
                    os.startfile(os.path.join(music_dir, songs))

        elif 'joke' in query or 'make me laugh' in query:
                speak(pyjokes.get_joke())

        elif 'who made you' in query or 'who created you' in query:
                speak("I have been created by Team Tech (Mantasha, Mahima, Shashank❤.")


        elif 'remember' in query:
            speak("what should I remember?")
            query = takeCommand()
            print(query)
            speak("you said me to remember that" +query)
            remember = open('query.txt','w')
            remember.write(query)
            remember.close()

        elif 'do you know anything' in query:
            try:
                remember = open('query.txt','r')
                speak("you said me to remember that" +remember.read())
            except Exception as e:
                speak("sir you didn't said anything to remember")

        elif 'goodbye' in query or 'exit' in query or 'bye' in query or 'down' in query or 'shutdown' in query or 'keep quiet' in query:
            speak("Do You want me to shutdown")
            query = takeCommand()
            if 'no' in query or 'cancel' in query:
                speak("Process cancelled")
            if 'yes' in query or 'yep' in query or 'shutdown' in query:
                    hour = int(datetime.datetime.now().hour)
                    if hour>=0 and hour<18:
                        speak("Have a Nice day!")
                        exit()
                    elif hour>=18 and hour<24:
                        speak("Ok, good Night")
                        exit()
