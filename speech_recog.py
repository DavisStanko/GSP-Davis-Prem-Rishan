import speech_recognition
import speech_recognition as sr

r = sr.Recognizer()  # set r as recognizer
mic = sr.Microphone()  # initialize mic


class Recognizer:

    def listening(self):
        global recognized_speech

        try:
            with mic as source:
                r.adjust_for_ambient_noise(source)  # adjusting audio based on bg noise
                audio = r.listen(source)  # listening for speech from mic

                recognized_speech = r.recognize_google(audio)
                return recognized_speech

        except speech_recognition.UnknownValueError:
            recognized_speech = "Sorry, didn't understand that."
            return recognized_speech

    # method for setting entry as recognized speech
    def paste(self, entry):
        entry = str(recognized_speech)
        return entry


"""try:
    with mic as source:
        r.adjust_for_ambient_noise(source)  # adjusting audio based on bg noise
        audio = r.listen(source)  # listening for speech from mic

        recognized_speech = r.recognize_google(audio)
        print(recognized_speech)

except speech_recognition.UnknownValueError:
    recognized_speech = "Sorry, didn't understand that."
    print(recognized_speech)"""
