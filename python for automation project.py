import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init("sapi5")
voices = engine.getproperty("voices")
engine.setproperty("voice",voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    #12:00 - noon
    #1:00 pm - morning / 13:00 - afternoon
    #18:00 - evening
    if hour >=0 and hour<12:
        speak("Good morning my love")
    elif hour >=12 and hour<18:
         speak("Good afternoon my love")
    else:
        speak("Good evening my love")
    speak("Let me know how can I help you,what are you looking for")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening to you my love....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing your voice....")
        query = r.recognize_google(audio, language="en-US")
        print(f"My dear friend you said :{query}\n")

except Exception  as e:
    print("Love say that again please ....")
    return "None"

return query

def sendEmail(to, content):
    server = smtplip.SMTP("smtp.gmail.com",587)
    server.ehlo()
    server.starttls()
    server.login("mwirigijustice101@gmail.com","gracekaari78@gmail.com ")
    server.sendmail("gracekaari78@gmail.com",to,content)
    server.close()


if __name__ == "__main__":
    wishme()

    while True:
        query = takeCommand().lower()

        if "wikipedia" in query:
            speak("searching wikipedia....")
            query query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia ")
            print(results)
            speak(results)

        if "open notepad" in query:
            npath =









