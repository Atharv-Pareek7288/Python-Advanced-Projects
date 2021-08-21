import pyttsx3
import datetime
import speech_recognition as sr
import pyaudio
import wikipedia
import os
engine = pyttsx3.init('sapi5')
voices= engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Sir")
    

    elif hour>=12 and hour<18:
        speak("Good Afternoon Sir")
    
    else:
        speak('Good Evening Sir')

    speak("I am Zira. Please tell me how may I help you ")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone(device_index=0) as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try :
        print("recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f'user said: {query}\n')

    except Exception as e:
        print("say that again please...")
        return"None"
    return query        
    

    
if __name__=="__main__" :
    wishMe()
    
    while True:
        query = takeCommand().lower()
        
        if "wikipedia" in query:
            speak("Serching wikipedia...")
            query = query.replace('wikipedia', "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak (results)

        elif 'open Google' in query:
            opengoogle ="C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(opengoogle)


        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")


        elif 'open code' in query:
            codePath = "C:\\Users\\Atharv\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'open spotify' in query:
            spotify = "C:\\Users\\Atharv\\AppData\\Roaming\\Spotify\\Spotify.exe"
            os.startfile(spotify)
            speak("opening spotify")    

        elif 'stop' in query:
            speak ("ok sir have a good day")
            break      

      



            
         



  







 



 