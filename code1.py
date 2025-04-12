import pyttsx3 as p
import speech_recognition as sr
import google.generativeai as palm
from googleapiclient.discovery import build
import pytube

print("Started")
engine =p.init()
rate=engine.getProperty('rate')
engine.setProperty('rate',170)
#print(rate)

voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
#print(voices)

#engine.say("hello sir.  i am ai replica")
#engine.say("And created by team Ai replica")
#engine.runAndWait()

def speak(text):
   engine.say(text)
   engine.runAndWait()

def ai_respose(prompt): 

    palm.configure(api_key="")
    response = palm.chat(messages=[str(prompt)])
    return response.last

r=sr.Recognizer()

speak("I am ai version of team learner")
speak("how are you sir?")

with sr.Microphone() as source:
   r.energy_threshold=1000
   r.adjust_for_ambient_noise(source,1.2)
   print("listening")
   audio= r.listen(source)
   text=r.recognize_google(audio)
   print(text)

#if "bad" and "not good" and "bekar" in text:
 #  speak("How can change your mood??")
speak("What can i do for you??")

while True:
      with sr.Microphone() as source:
        r.energy_threshold=10000
        r.adjust_for_ambient_noise(source,1.2)
        print("listening")
        audio= r.listen(source)
        text=r.recognize_google(audio)
        print(text)
        if text =="bye" or text=="quit" or text =="exit":
            break
        response = ai_respose(text)
        print("Response")
        print(response)
        speak(response)
        speak("What's next sir  ")

def play_video_on_youtube(command):
    # Extract video title from command
    video_title = command.split("play")[-1].strip()

    # Search for video on YouTube
    youtube = pytube.YouTube(f"https://www.youtube.com/results?search_query={video_title}")

    # Download the first video result
    video = youtube.streams.first()
    video.download()

    # Play the downloaded video
    print("Playing video:", video.title)
    video.play()

if __name__ == "__main__":
    while True:
        # Recognize voice command
        command = recognize_speech()

        # If command is "play video", search and play the video
        if command.startswith("play video"):
            play_video_on_youtube(command)
