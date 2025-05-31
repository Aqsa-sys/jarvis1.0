import pyttsx3 #pip install pyttsx3
import speech_recognition as sr 

def initialize_engine():
    engine = pyttsx3.init("sapi5")
    voices = engine.getProperty("voices")
    engine.setProperty('Voice', voices[1].id)
    engine.getProperty('rate')
    rate = engine.getProperty('rate')
    engine.setProperty('rate',rate-60)
    volume = engine.getProperty('volume')
    engine.setProperty('volume',min(volume + 0.25, 1.0))
    return engine
def speak(text):
    engine = initialize_engine()
    
    engine.say(text)
    engine.runAndWait()

    speak("Hello, I am Eva")