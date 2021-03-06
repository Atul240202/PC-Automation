#!/usr/bin/env python
# coding: utf-8
import pyttsx3           # It is a text-to-speech conversion library
import speech_recognition as sr     #Speech recognition library
import datetime as dt     #Used for greeting by Enigma
import wikipedia     #wikipedia access library
import webbrowser    #access default browser
import os       #acess laptop data location as specified
import requests     
import random
import smtplib     #Email related automation library for the actual sending function
import time       #for setting remainder
import sys       #interact with device
from email.message import EmailMessage     #Import the email modules we'll need




#voice output setup from enigma
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
rate = engine.getProperty('rate')   # getting details of current speaking rate                        #printing current voice rate
engine.setProperty('rate', 200)
engine.setProperty('voices', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

#defining greet function
def greet():
    hour = int(dt.datetime.now().hour)
    if hour>=4 and hour<=12:
        speak('Good Morning')
    elif hour>12 and hour<18:
        speak('Good Afternoon')
    elif hour>18 and hour<24:
        speak('Good Evening')
    speak('Enigma here, How may I help You?')

#for getting input
def takeCommand():
    
    r = sr.Recognizer()
    with sr.Microphone() as source:                # use the default microphone as the audio source
        audio = r.listen(source) 
        print("Listening...")
        r.pause_threshold = 0.5
        audio = r.listen(source)
    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")  

#if enigma is unable to take input
    except Exception as e:  
        print("Say that again please...")  
        return takeCommand() 
    return query





if __name__ == "__main__":
    greet()
    while True:

#for taking all the input in lowercase        
        query = takeCommand().lower()

#all wikipedia related search    
        if 'wikipedia' in query:
            speak('Searching wikipedia')
            query = query.replace("wikipedia", " ")
            results = wikipedia.summary(query, sentences=2)
            speak('According to wikipedia')
            speak(results)
            speak('What else I can do for you')


#for searching video on youtube            
        elif 'youtube' in query:
            speak("What should I search")
            search_content = takeCommand()                
            youtube_search = webbrowser.open('https://www.youtube.com/results?search_query=' + search_content)
            speak('What else I can do for you')


#for searching profile on github
        elif 'github' in query:
            speak("Whose repo do you wan't to open?")
            github_search = takeCommand()
            github_search = webbrowser.open('https://www.github.com/' + github_search)


#for checking weather using open weather API
        elif 'check weather' in query:
            api_address='http://api.openweathermap.org/data/2.5/weather?appid=e35a90f7c24c388e8eb9a27109ce40fd&q='
            speak("Which city?")
            city = takeCommand()
            url = api_address + city
            json_data = requests.get(url).json()
            format_add = json_data['weather'][0]['main']
            speak("Weather bole toh" + format_add)
            print("Weather bole toh" + format_add)


#for stackoverflow related searches
        elif 'stack overflow' in query:
            speak("What are you searching for?")
            overflow_search = takeCommand()
            Stack_search = webbrowser.open('https://stackoverflow.com/search?q=' + overflow_search)
            speak('What else I can do for you')
 
        
#for google searches 
        elif 'google' in query:
            speak("What do you want to google?")
            google_search = takeCommand()
            webbrowser.open('https://google.com/?#q=' + google_search)
            speak('What else I can do for you')
            


#for accessing music folder in device but for this we have to specify exact folder location            
        elif 'music' in query:
            music_folder = 'C:\\Users\\ATUL\\Music'
            songs = os.listdir(music_folder)
            print(songs)
            os.startfile(os.path.join(music_folder, random.choice(songs)))
            speak('What else I can do for you')


#for getting time        
        elif 'time' in query:
            Time_now = dt.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {Time_now}")
            print(f"Sir, the time is {Time_now}")
            speak('What else I can do for you')


#for opening sublime text from device if it is present in program files             
        elif 'sublime' in query:
            compiler_path = "C:\\Program Files\\Sublime Text 3\\sublime_text.exe"
            os.startfile(compiler_path)
            speak('What else I can do for you')


#for setting up remainder        
        elif 'reminder' in query:
            speak("What shall I remind you about?")
            text = takeCommand()
            speak("In how many minutes?")
            local_time = float(takeCommand())
            local_time = local_time * 60
            time.sleep(local_time)
            speak(text)
            speak('What else I can do for you')


#for doing email related automation but it need some more changes as its not yet user friendly        
        elif 'mail' in query:
            try:
                msg = EmailMessage()
                speak("What should I say?")
                content = takeCommand()
                msg.set_content(content)
                speak("What is the subject?")
                sub = takeCommand()
                msg['Subject'] = sub
                msg['From'] = "automation.testing87@gmail.com"
                speak("Whom you want to send?")
                reciepient = {"Atul": "jhark523@gmail.com", "second email": "jhaatul915@gmail.com", "college id": "19bcs1752@gmail.com",
                         "outlook": "19BCS1752@cuchd.in"}
                reciever = reciepient[takeCommand()]
                msg['To'] = reciever
                server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                server.login("automation.testing87@gmail.com", "Kumar@345")
                server.send_message(msg)
                speak("Email has been sent")
            except Exception as e:
                print(e)
                speak("Unable to send mail")
            speak('What else I can do for you')


#for shutting down enigma        
        elif 'shutdown' in query:
            speak("It was pleasure working for you")
            sys.exit("Thankyou")


#for asking enigma to take some break        
        elif 'break' in query:
            speak("How many minutes should I take a break?")
            minutes = float(takeCommand())
            minutes = minutes *60
            time.sleep(minutes)
            speak('I am Back, Sir')




