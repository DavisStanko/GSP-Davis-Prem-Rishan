# Import the required module for text
# to speech conversion
from tkinter import *
import tkinter.ttk as ttk
from gtts import gTTS
from deep_translator import GoogleTranslator
import playsound
import textwrap

ttk.output = ""

choose_langauge = {'af': 'afrikaans', 'sq': 'albanian', 'am': 'amharic', 'ar': 'arabic', 'hy': 'armenian',
                   'az': 'azerbaijani', 'eu': 'basque', 'be': 'belarusian', 'bn': 'bengali', 'bs': 'bosnian',
                   'bg': 'bulgarian', 'ca': 'catalan', 'ceb': 'cebuano', 'ny': 'chichewa',
                   'zh-cn': 'chinese (simplified)', 'zh-tw': 'chinese (traditional)', 'co': 'corsican',
                   'hr': 'croatian', 'cs': 'czech', 'da': 'danish', 'nl': 'dutch', 'en': 'english', 'eo': 'esperanto',
                   'et': 'estonian', 'tl': 'filipino', 'fi': 'finnish', 'fr': 'french', 'fy': 'frisian',
                   'gl': 'galician', 'ka': 'georgian', 'de': 'german', 'el': 'greek', 'gu': 'gujarati',
                   'ht': 'haitian creole', 'ha': 'hausa', 'haw': 'hawaiian', 'iw': 'hebrew', 'hi': 'hindi',
                   'hmn': 'hmong', 'hu': 'hungarian', 'is': 'icelandic', 'ig': 'igbo', 'id': 'indonesian',
                   'ga': 'irish', 'it': 'italian', 'ja': 'japanese', 'jw': 'javanese', 'kn': 'kannada', 'kk': 'kazakh',
                   'km': 'khmer', 'ko': 'korean', 'ku': 'kurdish (kurmanji)', 'ky': 'kyrgyz', 'lo': 'lao',
                   'la': 'latin', 'lv': 'latvian', 'lt': 'lithuanian', 'lb': 'luxembourgish', 'mk': 'macedonian',
                   'mg': 'malagasy', 'ms': 'malay', 'ml': 'malayalam', 'mt': 'maltese', 'mi': 'maori', 'mr': 'marathi',
                   'mn': 'mongolian', 'my': 'myanmar (burmese)', 'ne': 'nepali', 'no': 'norwegian', 'ps': 'pashto',
                   'fa': 'persian', 'pl': 'polish', 'pt': 'portuguese', 'pa': 'punjabi', 'ro': 'romanian',
                   'ru': 'russian', 'sm': 'samoan', 'gd': 'scots gaelic', 'sr': 'serbian', 'st': 'sesotho',
                   'sn': 'shona', 'sd': 'sindhi', 'si': 'sinhala', 'sk': 'slovak', 'sl': 'slovenian', 'so': 'somali',
                   'es': 'spanish', 'su': 'sundanese', 'sw': 'swahili', 'sv': 'swedish', 'tg': 'tajik', 'ta': 'tamil',
                   'te': 'telugu', 'th': 'thai', 'tr': 'turkish', 'uk': 'ukrainian', 'ur': 'urdu', 'uz': 'uzbek',
                   'vi': 'vietnamese', 'cy': 'welsh', 'xh': 'xhosa', 'yi': 'yiddish', 'yo': 'yoruba', 'zu': 'zulu',
                   'fil': 'Filipino', 'he': 'Hebrew'}


def get_key(val):
    for key, value in choose_langauge.items():
        if val == value:
            return key


def lang_options():
    global ttk

    lang = get_key(option_variable.get())
    print(lang)

    GoogleTranslator(source="auto", target=lang).translate(entry.get(1.0, "end"))


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
labelTittle.place(x=260, y=25)

# copy/paste https://stackoverflow.com/questions/36990396/automatically-copy-tkinter-text-widget-content-to-clipboard
# Flag stuff in options https://morioh.com/p/f900651c5e48


entryValue = StringVar()
option_variable = StringVar()
option_variable.set("English")

entry = Text(root, width=30, height=10, borderwidth=5, relief=RIDGE)

my_wrap = StringVar(value='none')

entry = Text(root, width=30, height=10, borderwidth=5, relief=RIDGE, wrap='word')

entry.place(x=10, y=100)

options = ttk.OptionMenu(root, option_variable, *choose_langauge.values())
options.place(x=550, y=105)

speak = ttk.Button(text="Speak", command=speak).place(x=325, y=450)

result = Label(root, width=30, height=10, anchor=NW, borderwidth=5, relief=RIDGE, wraplength=300, justify=LEFT)

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
