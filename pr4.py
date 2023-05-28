import json, apiai
import os

import pyttsx3
import speech_recognition as sr
tts = pyttsx3.init()
rate = tts.getProperty('rate')
tts.setProperty('rate', rate-40)
volume = tts.getProperty('volume')
tts.setProperty('volume', volume+0.9)
voices = tts.getProperty('voices')
tts.setProperty('voice', 'ru')
for voice in voices:
    if voice.name == 'Anna':
        tts.setProperty('voice', voice.id)

def record_volume():
    r = sr.Recognizer()
    device_index = 15
    with sr.Microphone(device_index) as source:
        print('Loading')
        print('Listening...')
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    print('Understood')
    try:
        query = r.recognize_google(audio)
        text = query.lower()
        if(text == "current"):
            print("Current directory:", os.getcwd())
        if(text == "create"):
            os.makedirs("nested1/nested2/nested3")
            print("Create new folders: ",  os.getcwd(), "/nested1/nested2/nested3")
        if(text == "back"):
            os.chdir("..")
            print("Previos directory", os.getcwd())
        print(f'You said: {text}')
    except:
        print('Error')

while True:
    record_volume()