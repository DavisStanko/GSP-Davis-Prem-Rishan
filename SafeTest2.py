# Import the required module for text
# to speech conversion
from tkinter import *
import tkinter.ttk as ttk
from gtts import gTTS
import PIL
from deep_translator import GoogleTranslator
import playsound

ttk.output = ""


def lang_options():
    global output
    option = option_variable.get()
    if option == "English":
        # translator
        ttk.output = GoogleTranslator(source='auto', target="en").translate(entry.get("1.0", "end-1c"))
    elif option == "French":
        # translator
        ttk.output = GoogleTranslator(source='auto', target="fr").translate(entry.get("1.0", "end-1c"))
    elif option == "Spanish":
        # translator
        ttk.output = GoogleTranslator(source='auto', target="es").translate(entry.get("1.0", "end-1c"))
    elif option == "Mandarin":
        # translator
        ttk.output = GoogleTranslator(source='auto', target="zh-CN").translate(entry.get("1.0", "end-1c"))


def speak():
    lang_options()

    result.config(text=ttk.output)

    # Passing the text and language to the engine,
    # here we have marked slow=False. Which tells
    # the module that the converted audio should
    myobj = gTTS(text=ttk.output, slow=False)

    # Saving the converted audio in a mp3 file named
    # welcome
    myobj.save("speech.mp3")

    # Playing the converted file
    playsound.playsound('speech.mp3', True)


def clear():
    entry.delete(1.0, 'end')
    result.config(text="")


def copy():
    global output
    root.clipboard_clear()
    root.clipboard_append(result["text"])


def switch():
    global is_on
    if is_on:
        onButton.config(image=off)
        is_on = False
        root.tk.call("set_theme", "light")
        copy.config(image=copyLight)
    else:
        onButton.config(image=on)
        is_on = True
        root.tk.call("set_theme", "dark")
        copy.config(image=copyDark)

#


root = Tk()

root.geometry("700x500")
root.title("Translate")
root.resizable(False, False)

# Dark/Light mode toggle
is_on = True
on = PhotoImage(file="dark.png")
off = PhotoImage(file="light.png")

onButton = Button(root, image=on, bd=0, cursor="hand2", command=switch)
onButton.place(x=630, y=25)
#


root.tk.call("source", "azure.tcl")
root.tk.call("set_theme", "dark")


labelTittle = ttk.Label(root, text="Translator", font=('Helvetica', 32, 'underline'))
labelTittle.place(x=250, y=25)


# copy/paste https://stackoverflow.com/questions/36990396/automatically-copy-tkinter-text-widget-content-to-clipboard
# stuff like googletrans and messagebox could be useful https://codingshiksha.com/python/python-tkinter-gui-script-to-make-language-translate-app-using-google-translate-api-full-project-for-beginners/
# Flag stuff in options https://morioh.com/p/f900651c5e48


entryValue = StringVar()
option_variable = StringVar()
option_variable.set("English")


entry = Text(root, width=30, height=10, borderwidth=5, relief=RIDGE)
entry.place(x=10, y=100)


<<<<<<< HEAD
options = ttk.OptionMenu(root, option_variable, 'Afrikaans',
                         'Albanian',
                         'Arabic',
                         'Armenian',
                         ' Azerbaijani',
                         'Basque',
                         'Belarusian',
                         'Bengali',
                         'Bosnian',
                         'Bulgarian',
                         ' Catalan',
                         'Cebuano',
                         'Chichewa',
                         'Chinese',
                         'Corsican',
                         'Croatian',
                         ' Czech',
                         'Danish',
                         'Dutch',
                         'English',
                         'Esperanto',
                         'Estonian',
                         'Filipino',
                         'Finnish',
                         'French',
                         'Frisian',
                         'Galician',
                         'Georgian',
                         'German',
                         'Greek',
                         'Gujarati',
                         'Haitian Creole',
                         'Hausa',
                         'Hawaiian',
                         'Hebrew',
                         'Hindi',
                         'Hmong',
                         'Hungarian',
                         'Icelandic',
                         'Igbo',
                         'Indonesian',
                         'Irish',
                         'Italian',
                         'Japanese',
                         'Javanese',
                         'Kannada',
                         'Kazakh',
                         'Khmer',
                         'Kinyarwanda',
                         'Korean',
                         'Kurdish',
                         'Kyrgyz',
                         'Lao',
                         'Latin',
                         'Latvian',
                         'Lithuanian',
                         'Luxembourgish',
                         'Macedonian',
                         'Malagasy',
                         'Malay',
                         'Malayalam',
                         'Maltese',
                         'Maori',
                         'Marathi',
                         'Mongolian',
                         'Myanmar',
                         'Nepali',
                         'Norwegian'
                         'Odia',
                         'Pashto',
                         'Persian',
                         'Polish',
                         'Portuguese',
                         'Punjabi',
                         'Romanian',
                         'Russian',
                         'Samoan',
                         'Scots Gaelic',
                         'Serbian',
                         'Sesotho',
                         'Shona',
                         'Sindhi',
                         'Sinhala',
                         'Slovak',
                         'Slovenian',
                         'Somali',
                         'Spanish',
                         'Sundanese',
                         'Swahili',
                         'Swedish',
                         'Tajik',
                         'Tamil',
                         'Tatar',
                         'Telugu',
                         'Thai',
                         'Turkish',
                         'Turkmen',
                         'Ukrainian',
                         'Urdu',
                         'Uyghur',
                         'Uzbek',
                         'Vietnamese',
                         'Welsh',
                         'Xhosa'
                         'Yiddish',
                         'Yoruba',
                         'Zulu',)
=======
options = ttk.OptionMenu(root, option_variable, "English", "English", "French", "Spanish", "Mandarin")
>>>>>>> b4f86c07f0e859a54c0177b25a5ffc75d8350000
options.place(x=550, y=105)


speak = ttk.Button(text="Speak", command=speak).place(x=325, y=450)


result = Label(root, width=30, height=10, anchor=NW, borderwidth=5, relief=RIDGE)
result.place(x=260, y=100)

clear = ttk.Button(root, text="Clear", cursor="hand2",
                   command=clear)
clear.place(x=280, y=300)

copyDark = PhotoImage(file="copy-d.png")
copyLight = PhotoImage(file="copy-l.png")

copy = Button(root, image=copyDark, bd=0, cursor="hand2",
              command=copy)
copy.place(x=180, y=300)


root.mainloop()
