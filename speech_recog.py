import speech_recognition
import speech_recognition as sr

r = sr.Recognizer()  # set r as recognizer
mic = sr.Microphone()  # initialize mic


class ListenError(Exception):
    """Class where you can print errors based on where called"""


class Recognizer:
    def __init__(self):
        self._start_listen = None

    def listen(self):
        global recognized_speech

        if self.listen() is not None:
            raise ListenError("Recognizer not listening.")

        try:
            with mic as source:
                r.adjust_for_ambient_noise(source)  # adjusting audio based on bg noise
                audio = r.listen(source)  # listening for speech from mic

                recognized_speech = r.recognize_google(audio)

        except speech_recognition.UnknownValueError:
            recognized_speech = "Sorry, didn't understand that."

    # method for setting entry as recognized speech
    def paste(self, entry):
        entry = recognized_speech
