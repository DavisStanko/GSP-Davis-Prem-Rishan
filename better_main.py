# Import the required module for text
# to speech conversion
from tkinter import *
import tkinter.ttk as ttk
from gtts import gTTS
from deep_translator import GoogleTranslator
import playsound

output = ""
def lang_options():
    global output
    option = option_variable.get()
    if option == "English":
        # translator
        output = GoogleTranslator(source='auto', target="en").translate(entry.get())
    elif option == "French":
        # translator
        output = GoogleTranslator(source='auto', target="fr").translate(entry.get())
    elif option == "Spanish":
        # translator
        output = GoogleTranslator(source='auto', target="es").translate(entry.get())
    elif option == "Mandarin":
        # translator
        output = GoogleTranslator(source='auto', target="zh-CN").translate(entry.get())

def speak():
    lang_options()

    result.config(text=output, fg="white")

    # Passing the text and language to the engine,
    # here we have marked slow=False. Which tells
    # the module that the converted audio should
    myobj = gTTS(text=output, slow=False)

    # Saving the converted audio in a mp3 file named
    # welcome
    myobj.save("speech.mp3")

    # Playing the converted file
    playsound.playsound('speech.mp3', True)



root = Tk()
ttk.Style().theme_use('clam')

root.geometry("700x500")
root.title("Translate")
root.resizable(False, False)

prompt = Label(text="Enter Your Birthday:")

entryValue = StringVar()
option_variable = StringVar()
option_variable.set("English")

entry = ttk.Entry(root, textvariable=entryValue, width=20)
entry.place(x=50, y=100)
# , width=20, bd=3, font=20, bg="#5B5750", fg="#FFF1BF"
options = OptionMenu(root, option_variable, "English", "French", "Spanish", "Mandarin")
options.place(x=450, y=105)

submit = Button(text="Speak", font=20, bg="#492C1D", fg="white", width=10, height=2, command=speak).place(x=325, y=450)

result = Label(text="", fg="white")
result.place(x=50, y=250)

root.mainloop()


