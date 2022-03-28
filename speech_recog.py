import speech_recognition as sr

# https://realpython.com/python-speech-recognition/#how-speech-recognition-works-an-overview
# https://ports.macports.org/port/flac/

r = sr.Recognizer()

harvard =sr.AudioFile("harvard.mp3")
with harvard as source:
    audio = r.record(source)

r.recognize_google(audio)
