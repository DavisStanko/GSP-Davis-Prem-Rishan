# Import the required module for text
# to speech conversion
from tkinter import *
from gtts import gTTS
from googletrans import Translator
# This module is imported so that we can
# play the converted audio
import playsound


def speak():
    # Language in which you want to convert
    language = 'en'

    # translator
    translator = Translator()
    output = translator.translate(translate_entry.get())

    result.config(text=output.text, fg="white")

    # Passing the text and language to the engine,
    # here we have marked slow=False. Which tells
    # the module that the converted audio should
    # have a high speed
    myobj = gTTS(text=entry.get() or output.text, lang=language, slow=False)

    # Saving the converted audio in a mp3 file named
    # welcome
    myobj.save("speech.mp3")

    # Playing the converted file
    playsound.playsound('speech.mp3', True)



root = Tk()
root.geometry("700x500")
root.resizable(False, False)

prompt = Label(text="Enter Your Birthday:")

entryValue = StringVar()
translateValue = StringVar()

entry = Entry(root, textvariable=entryValue, width=20, bd=3, font=20, bg="#5B5750", fg="#FFF1BF")
entry.place(x=370, y=200)

translate_entry = Entry(root, textvariable=translateValue, width=20, bd=3, font=20, bg="#5B5750", fg="#FFF1BF")
translate_entry.place(x=70, y=200)

submit = Button(text="Speak", font=20, bg="#492C1D", fg="white", width=10, height=2, command=speak).place(x=325, y=450)

result = Label(text="fads", fg="white")
result.place(x=100, y=100)

root.mainloop()


