import speech_recognition as sr

# https://realpython.com/python-speech-recognition/#how-speech-recognition-works-an-overview
# https://ports.macports.org/port/flac/

r = sr.Recognizer()
mic = sr.Microphone(device_index=0)


print(mic)

harvard = sr.AudioFile("harvard.wav")
with harvard as source:
    audio = r.record(source)

print(r.recognize_google(audio))

# print works on own computer, not sure how to test at school since we cannot use flac
# ok lets go db
