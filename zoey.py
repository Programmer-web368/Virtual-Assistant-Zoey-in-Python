import os
import sys
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import random


engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice', voices[1].id)





def speak(audio):                
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour<=1  and  hour>=12:
        speak("Good Morning")
    elif hour>=12  and  hour<=18:
        speak("Good Afternoon")

    else:
        speak("Good Evening") 

    speak("i am Zoey, how may i help you")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source: 
        print("Listening..")
        r.pause_threshold = 1
        audio = r.listen(source)
        
        try:
            print("Recognizing..")
            query = r.recognize_google(audio, language='en-in')
            print(f"User Said: {query}\n")
        except Exception as e:
            print(e)
            speak("I Can't Understand your command")
            return "None"
        return query
   
            




if __name__ == '__main__':
    wishMe()
    while True:
           query = takeCommand().lower()
           if  'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
            
                                                                                                                                                                                                                                                                                                                                                                                                                                                   
           elif 'open facebook' in query:
               webbrowser.open("facebook.com")
           
           elif 'open google' in query:
               webbrowser.open("google.com")
           
           elif 'open youtube' in query:
               webbrowser.open("youtube.com")  
               speak("open youtube")
               
           elif 'gana chalao' in query:
                music_dir = 'F:\\Downloads\\Music'
                songs = os.listdir(music_dir)
                os.startfile(os.path.join(music_dir, songs[7]))
                
           elif 'the time' in query:
                strTime = datetime.datetime.now().strftime("%H:%M")
                speak(f"Sir, the time is{strTime}") 
                           
           elif 'you are so sweet' in query:
                speak("Thank you Sir")
                
           elif 'what is my name' in query:
                speak("Sir, your name is Shahzaib")
                    
           elif 'what is your name' in query:
                speak("my name is Zoey") 
           
           elif 'what is your boss name' in query:
                speak("My boss name Shahzaib")
                
           elif 'what is your favourite colour' in query:
                speak("my favourite colour is red!")  
            
                             
            
           elif 'what is my friend name' in query:
                speak("Sir, your friend name is Mazhar, Muzammil and Tajammal.")
           
           elif 'open chrome' in query:
                chromePath = "C:\\Users\shahz\\AppData\\Local\\Google\\Chrome\\Application\\chrome.exe" 
                os.startfile(chromePath)             
            