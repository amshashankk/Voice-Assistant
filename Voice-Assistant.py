
import speech_recognition as sr
import datetime
import wikipedia 
import webbrowser
import os
import smtplib 
from gtts import gTTS
import playsound

def speak(text):
    tts = gTTS(text=text, lang="en-US")
    filename ="voice.mp3"
    tts.save(filename)
    playsound.playsound(filename)



def wishMe(): #this line will give command to assistant to wish you before you speak
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    elif hour>=17 and hour<20:
        speak("Good Evening")
    else:
        speak("Good Night!")         

def takeCommand(): # this line will refer you to say some command to do
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...") 
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('usermail', 'userpassword')
    server.sendmail(to, content)
    server.close()

if __name__ == "__main__":
    speak("Hello Sir, How may I help you !")
    

    query = takeCommand().lower()

       
if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

elif 'open youtube' in query:
            webbrowser.open("youtube.com")

elif 'open google' in query:
            webbrowser.open("google.com")

elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")   


elif 'play music' in query:
            music_dir = 'music path'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[2]))

elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

elif 'open code' in query:
            codePath = "user_vscode path"
            os.startfile(codePath)

elif 'email to user' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "recipientmail"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry I am unable to send the email")
elif 'exit' in query:
            exit() 
