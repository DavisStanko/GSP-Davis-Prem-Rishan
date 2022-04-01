from tkinter import *  # GUI
import tkinter.ttk as ttk  # Themes
from gtts import gTTS  # Google text to speech
from deep_translator import GoogleTranslator  # Google Translator
import playsound  # Play speech
import sqlite3  # Storing past translations
import datetime  # Getting date of translation


def startup():
    global rg

    if start_value == 0:
        from module_switch import ImportBlocker
        import sys

        sys.meta_path = [ImportBlocker('speech_recog')]
        sys.meta_path = [ImportBlocker('history_gui')]
    elif start_value == 1:
        try:
            from speech_recog import Recognizer
        except ImportError:
            pass

        try:
            rg = Recognizer()
        except NameError:
            pass
    elif start_value == 2:
        try:
            import history_gui
        except ImportError:
            pass


# Google translate language codes and language names
choose_langauge = {"af": "Afrikaans", "sq": "Albanian", "am": "Amharic", "ar": "Arabic", "hy": "Armenian",
                   "az": "Azerbaijani", "eu": "Basque", "be": "Belarusian", "bn": "Bengali", "bs": "Bosnian",
                   "bg": "Bulgarian", "ca": "Catalan", "ceb": "Cebuano", "ny": "Chichewa",
                   "zh-CN": "Chinese (Simplified)", "zh-TW": "Chinese (Traditional)", "co": "Corsican",
                   "hr": "Croatian", "cs": "Czech", "da": "Danish", "nl": "Dutch", "en": "English", "eo": "Esperanto",
                   "et": "Estonian", "tl": "Filipino", "fi": "Finnish", "fr": "French", "fy": "Frisian",
                   "gl": "Galician", "ka": "Georgian", "de": "German", "el": "Greek", "gu": "Gujarati",
                   "ht": "Haitian Creole", "ha": "Hausa", "haw": "Hawaiian", "iw": "Hebrew", "hi": "Hindi",
                   "hmn": "Hmong", "hu": "Hungarian", "is": "Icelandic", "ig": "Igbo", "id": "Indonesian",
                   "ga": "Irish", "it": "Italian", "ja": "Japanese", "jw": "Javanese", "kn": "Kannada", "kk": "Kazakh",
                   "km": "Khmer", "ko": "Korean", "ku": "Kurdish (Kurmanji)", "ky": "Kyrgyz", "lo": "Lao",
                   "la": "Latin", "lv": "Latvian", "lt": "Lithuanian", "lb": "Luxembourgish", "mk": "Macedonian",
                   "mg": "Malagasy", "ms": "Malay", "ml": "Malayalam", "mt": "Maltese", "mi": "Maori", "mr": "Marathi",
                   "mn": "Mongolian", "my": "Myanmar (Burmese)", "Me": "Npali", "no": "Norwegian", "ps": "Pashto",
                   "fa": "Persian", "pl": "Polish", "pt": "Portuguese", "pa": "Punjabi", "ro": "Romanian",
                   "ru": "Russian", "sm": "Samoan", "gd": "Scots Gaelic", "sr": "Serbian", "st": "Sesotho",
                   "sn": "Shona", "sd": "Sindhi", "si": "Sinhala", "sk": "Slovak", "sl": "Slovenian", "so": "Somali",
                   "es": "Spanish", "su": "Sundanese", "sw": "Swahili", "sv": "Swedish", "tg": "Tajik", "ta": "Tamil",
                   "te": "Telugu", "th": "Thai", "tr": "Turkish", "uk": "Ukrainian", "ur": "Urdu", "uz": "Uzbek",
                   "vi": "Vietnamese", "cy": "Welsh", "xh": "Xhosa", "yi": "Yiddish", "yo": "Yoruba", "zu": "Zulu",
                   "fil": "Filipino", "he": "Hebrew"}

d_l_buttons = 0

start_value = 0


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
    input_get = entry.get("1.0", "end-1c")
    translatedResult = result["text"]
    lang = option_variable.get()
    current_date_time = (datetime.datetime.now())
    date = current_date_time.strftime("%Y-%m-%d")
    hours = current_date_time.strftime("%H:%M:%S")
    if len(input_get) == 0:
        return
    else:
        values = (input_get, translatedResult, lang, date)
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
        myobj.save("speech.mp3")  # Saving the converted audio in a mp3 file
        playsound.playsound("speech.mp3", True)  # Playing the converted file
    except ValueError:
        # Passing the text and language, speed, and accent to gtts
        myobj = gTTS(text=ttk.output, slow=False, lang="en")
        myobj.save("speech.mp3")  # Saving the converted audio in a mp3 file
        playsound.playsound("speech.mp3", True)  # Playing the converted file
    except AssertionError:
        pass


def clear():  # Clear both text boxes
    entry.delete(1.0, "end")
    result.config(text="")


def copy():  # Copy the text
    window.clipboard_clear()
    window.clipboard_append(result["text"])
    window.update()


def switch():  # Switch the theme
    global dark_mode, d_l_buttons
    if dark_mode:
        onButton.config(image=off)
        dark_mode = False
        window.tk.call("set_theme", "light")
        copy.config(image=copy_light)
        mic_button.config(image=mic_light)
        history.config(image=history_light)
        d_l_buttons = 1

    else:
        onButton.config(image=on)
        dark_mode = True
        window.tk.call("set_theme", "dark")
        copy.config(image=copy_dark)
        mic_button.config(image=mic_dark)
        history.config(image=history_dark)
        d_l_buttons = 0


def submit_Button():
    try:  # puts translated text to db file if speech fails
        submit()
    except:
        pass
    try:
        get_info()
    except:
        pass


# kinda works
def history_window():
    exec(open("./history_gui.py").read())


def enable_speech():
    global start_value

    start_value = 1
    mic_button.place(x=335, y=300)


def listen():
    global start_value
    start_value = 2
    mic_value = True

    entry.delete(1.0, "end")
    result.config(text="")

    rg.listening()
    detected = rg.paste(entryValue)
    entry.insert(END, detected)

    mic_value = False


def mic_enabled():
    global mic_value

    mic_value = True
    if mic_value:
        mic_button.config(image=mic_enable)
    else:
        pass


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

optionsAuto = ttk.Button(text="Auto Detect", state="disabled")
optionsAuto.place(x=160, y=105)

submit1 = ttk.Button(text="Submit", style="Accent.TButton", command=submit_Button)
submit1.place(x=250, y=450)

result = Label(window, width=35, height=20, anchor=NW,
               borderwidth=5, relief=RIDGE, wraplength=250, justify=LEFT)
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
mic_enable = PhotoImage(file="mic-green.png")

mic_value = False
mic_button = Button(window, image=mic_dark, bd=0, cursor="hand2", command=listen)

# Menu
upper_menu = Menu(window)
window.config(menu=upper_menu)
options_menu = Menu(upper_menu)
upper_menu.add_cascade(label="Options", menu=options_menu)
options_menu.add_command(label="Enable Speech", command=enable_speech)

# tempCreate = Button(window, text="Create", command=create_table)
# tempCreate.place(x=355, y=250)

startup()

window.mainloop()
