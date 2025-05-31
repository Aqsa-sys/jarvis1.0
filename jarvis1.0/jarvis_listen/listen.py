import speech_recognition as sr #pip install SpeechRecognition
import os #no need to install
import threading #no need to install
from mtranslate import translate
from colorama import Fore,Style, init   #pip translate mtranslate

init(autoreset=True) #automatically reset style after each print

def print_loop():
    while True:
       print(Fore.LIGHTGREEN_EX + "I am listening...", end="", flush=True)
       print(Style.RESET_ALL, end="", flush=True) 