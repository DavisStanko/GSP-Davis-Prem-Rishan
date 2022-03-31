import speech_recognition as sr

# https://realpython.com/python-speech-recognition/#how-speech-recognition-works-an-overview

r = sr.Recognizer()  # set r as recognizer
mic = sr.Microphone()  # initialize mic

with mic as source:
    audio = r.listen(source)  # listening for speech from mic

print(r.recognize_google(audio))
