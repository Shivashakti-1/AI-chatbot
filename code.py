import pyttsx3 as p
import speech_recognition as sr
import google.generativeai as palm

print("Started")
engine =p.init()
rate=engine.getProperty('rate')
engine.setProperty('rate',180)
print(rate)

voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
print(voices)

engine.say("hello sir.  i am ai replica")
engine.say("And created by team Ai replica")
#,,engine.runAndWait()

def speak(text):
   engine.say(text)
   engine.runAndWait()

def ai_respose(prompt):

    palm.configure(api_key="")
    response = palm.chat(messages=[str(prompt)])
    return response.last

r=sr.Recognizer()

speak("I am ai replica , and created by team Ai replica")
speak("how are you sir?")

with sr.Microphone() as source:
   r.energy_threshold=10000
   r.adjust_for_ambient_noise(source,1.2)
   print("listening")
   audio= r.listen(source)
   text=r.recognize_google(audio)
   print(text)

if "what" and "about" and "you" in text:
   speak("I am also having good day sir")
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
