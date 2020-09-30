#!/usr/bin/env python
# coding: utf-8

# In[12]:


import pyttsx3  #install this library using 'pip install pyttsx3' in your compiler terminal
import speech_recognition as sr #install this library using 'pip install SpeechRecognition' in your compiler terminal
import datetime as dt #Its an pre-installed library in Python
import wikipedia
import webbrowser
import os #Its an pre-installed library in Python
import random #Its an pre-installed library in Python
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def greet():
    hour = int(dt.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak('Good Morning')
    if hour>12 and hour<18:
        speak('Good Afternoon')
    else:
        speak('Good Evening')
    speak('I am Enigma, How may I help You?')

def takeCommand():
    
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
        print("Say that again please...")  
        return "None" 
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('automation.testing87@gmail.com', 'Kumar@345')
    server.sendmail('automation.testing87@gmail.com', to, content)
    server.close()
        

if __name__ == "__main__":
    greet()
    while True:
        
        query = takeCommand().lower()
    
        if 'wikipedia' in query:
            speak('Searching wikipedia')
            query = query.replace("wikipedia", " ")
            results = wikipedia.summary(query, sentences=2)
            print(results)
            speak('According to wikipedia')
            speak(results)
            
        elif 'youtube' in query:
            webbrowser.open('youtube.com')
        elif 'stack overflow' in query:
            webbrowser.open('stackoverflow.com')
        elif 'google' in query:
            webbrowser.open('google.com')
        elif 'music' in query:
            music_folder = 'C:\\Users\\Atul Jha\\Music\\One Direction - Midnight Memories (Deluxe)'
            songs = os.listdir(music_folder)
            print(songs)
            os.startfile(os.path.join(music_folder, random.choice(songs)))
        
        elif 'time' in query:
            Time_now = dt.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {Time_now}")
            
        elif 'sublime' in query:
            compiler_path = "C:\\Program Files\\Sublime Text 3\\sublime_text.exe"
            os.startfile(compiler_path)
        
        elif 'email' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "jhark523@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Unable to send mail")
        elif 'quit' in query:
            exit()


# In[ ]:




