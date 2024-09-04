import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia as wiki
import webbrowser
import os
import random
#import spotipy have to explore it first

engine = pyttsx3.init("sapi5")#to take win voice we use sapi5 api
voices = engine.getProperty('voices')#get a list of voices
engine.setProperty('voice',voices[1])
def speak(audio):
    engine.say(audio)
    engine.runAndWait()#do more research about it
# def conti():
#     speak("I'm listening...")
#     takeCommand()
#     return query1
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning")
        speak("I'm Pluto,how may I help you")
    elif hour>=12 and hour<18:
        speak("Good afternoon")
        speak("I'm Pluto,how may I help you")
    else:
        speak("Good evening")    
        speak("I'm Pluto,how may I help you")    
def takeCommand():
   #while(query1=='listen'): 
    #takes comd and returns
    r = sr.Recognizer()  # recognizer is a class to understand voice commands
    languages = ['en-IN', 'hi-IN']  # add Hindi language support
    for language in languages:
        with sr.Microphone() as source:  # system microphone use as src
            print("Listening...")
            r.pause_threshold = 2#self.pause_threshold isko bhi check krna h itll ignore noise
            r.energy_threshold=1000
            audio = r.listen(source)
            try:
                print("Recognizing...")
                query = r.recognize_google(audio, language=language)
                print(f"User said: {query}\n")  #finally got a backtik ka judwa bhai
            
            except Exception as e:
                #print(e) this line will show error ok
                print("Repeat it again please.....")
                return "none"       
            return query


if __name__ == '__main__':   
#  query1='listen'   
#  query1=conti()
# while (query1=='listen'):
   wishMe()
   query=takeCommand().lower()

  #logic to determine tasks that will be done by pluto
  ####################wikipedia for just dictionary or term or word search################
if 'wikipedia' in query:
    speak('Searching Wikipedia...')
    query = query.replace("wikipedia", "")
    try:
        results = wiki.summary(query, sentences=2)
        speak("According to Wikipedia")
        speak(results)
        try:
            print(results)
        except Exception as e:
            print("Unable to print the Wikipedia summary. Please try another topic.")
    except Exception as e:
        speak("Sorry, the Wikipedia page for that topic could not be found. Please try another topic.")
elif 'open code' in query:
    os.system("code .")  # Open Visual Studio Code
elif 'open powerpoint' in query:
    os.system("start powerpnt.exe")  # Open Microsoft PowerPoint (Windows only)
elif 'open excel' in query:
    os.system("start excel.exe")  # Open Microsoft Excel (Windows only)
elif 'open word art' in query:
    os.system("start wordart.exe")  # Open WordArt (Windows only)
elif 'open notepad' in query:
    os.system("start notepad")   # Open notepad
elif 'open chrome' in query:
    os.system("start chrome")    
elif 'open' in query:
    name = query.split(' ')[1]
    speak('Opening'+name)
    try:
        webbrowser.open(name+'.com')
    except Exception as e:
        speak("Sorry, I couldn't open the website. Please try another one.")     
elif 'search youtube' in query:
    name=query.split(' ')
    name.remove('search')
    name.remove('youtube')
    c=''
    for x in name:
       c+=' '+x
    speak('Showing results for '+c)
    try:
        webbrowser.open('https://www.youtube.com/results?search_query='+c)
    except Exception as e:
        speak("Sorry, I couldn't play the music. Please try another one.")
# elif 'play music' in query:
#     music_name = query.split(' ')[2]
#     speak('Playing '+music_name+' music...')
#     try:
#         sp = spotipy.Spotify(auth_token='your_token')
#         song = sp.start_song(music_name)
#     except Exception as e:
#         speak("Sorry, I couldn't play the music. Please try another one.")
# TO-DO: make a python code to get token from sportify each hour if previous token is expired. 
elif 'play music' in query:
       music_dir='D:\music'
       songs=os.listdir(music_dir)
       song = random.choice(songs)
       os.startfile(os.path.join(music_dir, song))      
elif "the time" in query:
    strTime = datetime.datetime.now().strftime("%H:%M:%S")#simply specify time in a format
    speak(f"The time is {strTime}")               
elif 'browse' in query:
    name=query.split(' ')
    name.remove('browse')
    c=''
    for x in name:
       c+=' '+x
    speak('Showing results for '+c)
    try:
        webbrowser.open('https://www.google.com/search?q='+c)
    except Exception as e:
        speak("Sorry, I couldn't browse that.")
