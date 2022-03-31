from tkinter import *  # GUI
import tkinter.ttk as ttk  # Themes
from gtts import gTTS  # Google text to speech
from deep_translator import GoogleTranslator  # Google Translator
import playsound  # Play speech
import sqlite3  # Storing past translations
import datetime  # Getting date of translation
"""from module_switch import ImportBlocker
import sys
sys.meta_path = [ImportBlocker('speech_recog')]
from speech_recog import Recognizer"""

# Google translate language codes and language names
choose_langauge = {"af": "afrikaans", "sq": "albanian", "am": "amharic", "ar": "arabic", "hy": "armenian", "az": "azerbaijani", "eu": "basque", "be": "belarusian", "bn": "bengali", "bs": "bosnian", "bg": "bulgarian", "ca": "catalan", "ceb": "cebuano", "ny": "chichewa", "zh-CN": "chinese (simplified)", "zh-TW": "chinese (traditional)", "co": "corsican", "hr": "croatian", "cs": "czech", "da": "danish", "nl": "dutch", "en": "english", "eo": "esperanto", "et": "estonian", "tl": "filipino", "fi": "finnish", "fr": "french", "fy": "frisian", "gl": "galician", "ka": "georgian", "de": "german", "el": "greek", "gu": "gujarati", "ht": "haitian creole", "ha": "hausa", "haw": "hawaiian", "iw": "hebrew", "hi": "hindi", "hmn": "hmong", "hu": "hungarian", "is": "icelandic", "ig": "igbo", "id": "indonesian", "ga": "irish", "it": "italian", "ja": "japanese", "jw": "javanese", "kn": "kannada", "kk": "kazakh", "km": "khmer", "ko": "korean", "ku": "kurdish (kurmanji)", "ky": "kyrgyz", "lo": "lao", "la": "latin", "lv": "latvian", "lt": "lithuanian", "lb": "luxembourgish", "mk": "macedonian", "mg": "malagasy", "ms": "malay", "ml": "malayalam", "mt": "maltese", "mi": "maori", "mr": "marathi", "mn": "mongolian", "my": "myanmar (burmese)", "ne": "nepali", "no": "norwegian", "ps": "pashto", "fa": "persian", "pl": "polish", "pt": "portuguese", "pa": "punjabi", "ro": "romanian", "ru": "russian", "sm": "samoan", "gd": "scots gaelic", "sr": "serbian", "st": "sesotho", "sn": "shona", "sd": "sindhi", "si": "sinhala", "sk": "slovak", "sl": "slovenian", "so": "somali", "es": "spanish", "su": "sundanese", "sw": "swahili", "sv": "swedish", "tg": "tajik", "ta": "tamil", "te": "telugu", "th": "thai", "tr": "turkish", "uk": "ukrainian", "ur": "urdu", "uz": "uzbek", "vi": "vietnamese", "cy": "welsh", "xh": "xhosa", "yi": "yiddish", "yo": "yoruba", "zu": "zulu", "fil": "Filipino", "he": "Hebrew"}

"rg = Recognizer()"


##################################

def create_product_table_UI():
    create_table()


def create_table():
    db_name = "translation_history.db"
    sql = """create table History
            (Input text,
            Translation text,
            Language text,
            Date text)"""
    table_name = "History"

    with sqlite3.connect(db_name) as db:
        cursor = db.cursor()
        cursor.execute("select name from sqlite_master where name=?", (table_name,))
        result = cursor.fetchall()
        keep_table = True
        if len(result) == 1:
            response = input("The table {0} already exists, do you wish to recreate it? (y/n): ".format(table_name))
            if response == "y":
                keep_table = False
                print("The {0} table will be recreated - all existing data will be lost.".format(table_name))
                cursor.execute("drop table if exists {0}".format(table_name))
                db.commit()
            else:
                print("The existing table was kept.")
        else:
            keep_table = False
            print("A new table was created.")

        # create the table if required (not keeping old one)
        if not keep_table:
            cursor.execute(sql)
            db.commit()


def insert_data(values):
    # global
    with sqlite3.connect("translation_history.db") as db:
        cursor = db.cursor()
        sql = "insert into History (Input, Translation, Language, Date) values (?,?,?,?)"
        cursor.execute(sql, values)
        db.commit()


def get_info():
    inputGet = entry.get("1.0", "end-1c")
    translatedResult = result["text"]
    lang = option_variable.get()
    current_date_time = (datetime.datetime.now())
    date = current_date_time.strftime("%Y-%m-%d")
    hours = current_date_time.strftime("%H:%M:%S")

    values = (inputGet, translatedResult, lang, date)
    insert_data(values)


def get_key(val):  # Get key from value
    for key, value in choose_langauge.items():
        if val == value:
            return key


def submit():  # Translate and display the text
    lang = get_key(option_variable.get())  # Get the output language
    ttk.output = GoogleTranslator(source="auto", target=lang).translate(entry.get(1.0, "end"))  # Translate the text
    result.config(text=ttk.output)
    try:
        # Passing the text and language, speed, and accent to gtts
        myobj = gTTS(text=ttk.output, slow=False, lang=lang)
        myobj.save("speech.mp3")  # Saving the converted audio in an mp3 file
        playsound.playsound("speech.mp3", True)  # Playing the converted file
    except ValueError:
        # Passing the text and language, speed, and accent to gtts
        myobj = gTTS(text=ttk.output, slow=False, lang="en")
        myobj.save("speech.mp3")  # Saving the converted audio in an mp3 file
        playsound.playsound("speech.mp3", True)  # Playing the converted file


def clear():  # Clear both text boxes
    entry.delete(1.0, "end")
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
        history_win.tk.call("set_theme", "light")
        copy.config(image=copy_light)
        mic_button.config(image=mic_light)
        history.config(image=history_light)
    else:
        onButton.config(image=on)
        dark_mode = True
        window.tk.call("set_theme", "dark")
        history_win.tk.call("set_theme", "dark")
        copy.config(image=copy_dark)
        mic_button.config(image=mic_dark)
        history.config(image=history_dark)


def submit_Button():
    submit()
    get_info()


def listen():
    rg.listening()
    rg.paste(entryValue)

def history_window():
    history_win = Tk()  # Create the window
    history_win.geometry("500x500")  # Set the size
    history_win.title("Translation History")  # Set the title
    history_win.resizable(True, True)  # Disable resizing
    history_win.tk.call("source", "azure.tcl")
    history_win.tk.call("set_theme", "dark")

    def close_history():
        history_win.destroy()

    close_button = ttk.Button(history_win, text="Close", cursor="hand2", style="Accent.TButton", command=close_history)
    close_button.place(x=250, y=450)



window = Tk()  # Create the window
window.geometry("700x500")  # Set the size
window.title("Translate")  # Set the title
window.resizable(True, True)  # Disable resizing

# Dark/Light mode toggle
dark_mode = True
on = PhotoImage(file="dark.png")
off = PhotoImage(file="light.png")
onButton = Button(window, image=on, bd=0, cursor="hand2", command=switch)
onButton.place(x=630, y=25)

# Default theme
window.tk.call("source", "azure.tcl")
window.tk.call("set_theme", "dark")

# Title
labelTittle = ttk.Label(window, text="Translator",
                        font=("Helvetica", 32, "underline"))
labelTittle.place(x=260, y=25)

entryValue = StringVar()
option_variable = StringVar()
option_variable.set("English")

entry = Text(window, width=35, height=20,
             borderwidth=5, relief=RIDGE, wrap="word")
entry.place(x=70, y=150)

options = ttk.OptionMenu(window, option_variable, *choose_langauge.values())
options.place(x=460, y=105)

option_variable2 = StringVar()
option_variable2.set("Auto Detect")

optionsAuto = ttk.OptionMenu(window, option_variable2, "Auto Detect", "Auto Detect")
optionsAuto.place(x=160, y=105)

submit1 = ttk.Button(text="Submit", style="Accent.TButton", command=submit_Button)
submit1.place(x=250, y=450)

result = Label(window, width=35, height=20, anchor=NW,
               borderwidth=5, relief=RIDGE, wraplength=300, justify=LEFT)
result.place(x=375, y=153)

clear = ttk.Button(window, text="Clear", cursor="hand2", style="Accent.TButton", command=clear)
clear.place(x=350, y=450)

# copy/paste https://stackoverflow.com/questions/36990396/automatically-copy-tkinter-text-widget-content-to-clipboard
copy_dark = PhotoImage(file="copy-d.png")
copy_light = PhotoImage(file="copy-l.png")

copy = Button(window, image=copy_dark, bd=0, cursor="hand2", command=copy)
copy.place(x=335, y=350)

history_dark = PhotoImage(file="history-d.png")
history_light = PhotoImage(file="history-l.png")

history = Button(window, image=history_dark, bd=0, cursor="hand2", command=history_window)
history.place(x=335, y=250)

mic_dark = PhotoImage(file="mic-d.png")
mic_light = PhotoImage(file="mic-l.png")

mic_button = Button(window, image=mic_dark, bd=0, cursor="hand2", command=listen)
mic_button.place(x=335, y=300)

# Things to do
# Fix up create table code, get history to open new window to display past translation history, make it show
# pre and post translation with language and time/date. Add option to clear database/history
# Make it easy to copy bits you need from history window
# mic func to rishans STT code
# In general make UI look tad nicer

# tempCreate = Button(window, text="Create", command=create_table)
# tempCreate.place(x=355, y=250)

window.mainloop()