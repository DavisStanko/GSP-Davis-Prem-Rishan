from tkinter import *  # GUI
import tkinter.ttk as ttk  # Themes
from gtts import gTTS  # Google text to speech
from deep_translator import GoogleTranslator  # Google Translator
import playsound  # Play speech

# Google translate language codes and language names
choose_langauge = {'af': 'afrikaans', 'sq': 'albanian', 'am': 'amharic', 'ar': 'arabic', 'hy': 'armenian', 'az': 'azerbaijani', 'eu': 'basque', 'be': 'belarusian', 'bn': 'bengali', 'bs': 'bosnian', 'bg': 'bulgarian', 'ca': 'catalan', 'ceb': 'cebuano', 'ny': 'chichewa', 'zh-CN': 'chinese (simplified)', 'zh-TW': 'chinese (traditional)', 'co': 'corsican', 'hr': 'croatian', 'cs': 'czech', 'da': 'danish', 'nl': 'dutch', 'en': 'english', 'eo': 'esperanto', 'et': 'estonian', 'tl': 'filipino', 'fi': 'finnish', 'fr': 'french', 'fy': 'frisian', 'gl': 'galician', 'ka': 'georgian', 'de': 'german', 'el': 'greek', 'gu': 'gujarati', 'ht': 'haitian creole', 'ha': 'hausa', 'haw': 'hawaiian', 'iw': 'hebrew', 'hi': 'hindi', 'hmn': 'hmong', 'hu': 'hungarian', 'is': 'icelandic', 'ig': 'igbo', 'id': 'indonesian', 'ga': 'irish', 'it': 'italian', 'ja': 'japanese', 'jw': 'javanese', 'kn': 'kannada', 'kk': 'kazakh', 'km': 'khmer', 'ko': 'korean', 'ku': 'kurdish (kurmanji)', 'ky': 'kyrgyz', 'lo': 'lao', 'la': 'latin', 'lv': 'latvian', 'lt': 'lithuanian', 'lb': 'luxembourgish', 'mk': 'macedonian', 'mg': 'malagasy', 'ms': 'malay', 'ml': 'malayalam', 'mt': 'maltese', 'mi': 'maori', 'mr': 'marathi', 'mn': 'mongolian', 'my': 'myanmar (burmese)', 'ne': 'nepali', 'no': 'norwegian', 'ps': 'pashto', 'fa': 'persian', 'pl': 'polish', 'pt': 'portuguese', 'pa': 'punjabi', 'ro': 'romanian', 'ru': 'russian', 'sm': 'samoan', 'gd': 'scots gaelic', 'sr': 'serbian', 'st': 'sesotho', 'sn': 'shona', 'sd': 'sindhi', 'si': 'sinhala', 'sk': 'slovak', 'sl': 'slovenian', 'so': 'somali', 'es': 'spanish', 'su': 'sundanese', 'sw': 'swahili', 'sv': 'swedish', 'tg': 'tajik', 'ta': 'tamil', 'te': 'telugu', 'th': 'thai', 'tr': 'turkish', 'uk': 'ukrainian', 'ur': 'urdu', 'uz': 'uzbek', 'vi': 'vietnamese', 'cy': 'welsh', 'xh': 'xhosa', 'yi': 'yiddish', 'yo': 'yoruba', 'zu': 'zulu', 'fil': 'Filipino', 'he': 'Hebrew'}


def get_key(val):  # Get key from value
    for key, value in choose_langauge.items():
        if val == value:
            return key


def submit():  # Translate and display the text
    lang = get_key(option_variable.get())  # Get the output language
    ttk.output = GoogleTranslator(source="auto", target=lang).translate(
        entry.get(1.0, "end"))  # Translate the text
    result.config(text=ttk.output)
    # Passing the text and language, speed, and accent to gtts
    myobj = gTTS(text=ttk.output, slow=False, lang=lang)
    myobj.save("speech.mp3")  # Saving the converted audio in an mp3 file
    playsound.playsound('speech.mp3', True)  # Playing the converted file


def clear():  # Clear both text boxes
    entry.delete(1.0, 'end')
    result.config(text="")


def copy():  # Copy the text
    window.clipboard_clear()
    window.clipboard_append(result["text"])


def switch():  # Switch the theme
    global dark_mode
    if dark_mode:
        onButton.config(image=off)
        dark_mode = False
        window.tk.call("set_theme", "light")
        copy.config(image=copyLight)
    else:
        onButton.config(image=on)
        dark_mode = True
        window.tk.call("set_theme", "dark")
        copy.config(image=copyDark)


window = Tk()  # Create the window
window.geometry("700x500")  # Set the size
window.title("Translate")  # Set the title
window.resizable(False, False)  # Disable resizing

# Dark/Light mode toggle
dark_mode = True
on = PhotoImage(file="dark.png")
off = PhotoImage(file="light.png")
onButton = Button(window, image=on, bd=0, cursor="hand2", command=switch)
onButton.place(x=630, y=25)

# Defualt theme
window.tk.call("source", "azure.tcl")
window.tk.call("set_theme", "dark")

# Title
labelTittle = ttk.Label(window, text="Translator",
                        font=('Helvetica', 32, 'underline'))
labelTittle.place(x=260, y=25)

entryValue = StringVar()
option_variable = StringVar()
option_variable.set("English")

entry = Text(window, width=35, height=20,
             borderwidth=5, relief=RIDGE, wrap='word')
entry.place(x=70, y=150)

options = ttk.OptionMenu(window, option_variable, *choose_langauge.values())
options.place(x=460, y=105)

submit = ttk.Button(text="Submit", command=submit)
submit.place(x=250, y=450)

result = Label(window, width=35, height=20, anchor=NW,
               borderwidth=5, relief=RIDGE, wraplength=300, justify=LEFT)
result.place(x=375, y=153)

clear = ttk.Button(window, text="Clear", cursor="hand2", command=clear)
clear.place(x=350, y=450)

# copy/paste https://stackoverflow.com/questions/36990396/automatically-copy-tkinter-text-widget-content-to-clipboard
copyDark = PhotoImage(file="copy-d.png")
copyLight = PhotoImage(file="copy-l.png")

copy = Button(window, image=copyDark, bd=0, cursor="hand2", command=copy)
copy.place(x=335, y=350)


window.mainloop()
