import speech_recognition
import speech_recognition as sr


r = sr.Recognizer()  # set r as recognizer
mic = sr.Microphone()  # initialize mic

try:
    with mic as source:
        r.adjust_for_ambient_noise(source)  # adjusting audio based on bg noise
        audio = r.listen(source)  # listening for speech from mic

        print(r.recognize_google(audio))

except speech_recognition.UnknownValueError:
    print("Sorry, didn't understand that.")


