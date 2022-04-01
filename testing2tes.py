from tkinter import *  # GUI
import tkinter.ttk as ttk  # Themes
from gtts import gTTS  # Google text to speech
from deep_translator import GoogleTranslator  # Google Translator
import playsound  # Play speech
import sqlite3  # Storing past translations
import datetime  # Getting date of translation
# import history_gui

"""from module_switch import ImportBlocker
import sys
sys.meta_path = [ImportBlocker('speech_recog')]

from speech_recog import Recognizer"""

# Google translate language codes and language names
choose_langauge = {"af": "afrikaans", "sq": "albanian", "am": "amharic", "ar": "arabic", "hy": "armenian", "az": "azerbaijani", "eu": "basque", "be": "belarusian", "bn": "bengali", "bs": "bosnian", "bg": "bulgarian", "ca": "catalan", "ceb": "cebuano", "ny": "chichewa", "zh-CN": "chinese (simplified)", "zh-TW": "chinese (traditional)", "co": "corsican", "hr": "croatian", "cs": "czech", "da": "danish", "nl": "dutch", "en": "english", "eo": "esperanto", "et": "estonian", "tl": "filipino", "fi": "finnish", "fr": "french", "fy": "frisian", "gl": "galician", "ka": "georgian", "de": "german", "el": "greek", "gu": "gujarati", "ht": "haitian creole", "ha": "hausa", "haw": "hawaiian", "iw": "hebrew", "hi": "hindi", "hmn": "hmong", "hu": "hungarian", "is": "icelandic", "ig": "igbo", "id": "indonesian", "ga": "irish", "it": "italian", "ja": "japanese", "jw": "javanese", "kn": "kannada", "kk": "kazakh", "km": "khmer", "ko": "korean", "ku": "kurdish (kurmanji)", "ky": "kyrgyz", "lo": "lao", "la": "latin", "lv": "latvian", "lt": "lithuanian", "lb": "luxembourgish", "mk": "macedonian", "mg": "malagasy", "ms": "malay", "ml": "malayalam", "mt": "maltese", "mi": "maori", "mr": "marathi", "mn": "mongolian", "my": "myanmar (burmese)", "ne": "nepali", "no": "norwegian", "ps": "pashto", "fa": "persian", "pl": "polish", "pt": "portuguese", "pa": "punjabi", "ro": "romanian", "ru": "russian", "sm": "samoan", "gd": "scots gaelic", "sr": "serbian", "st": "sesotho", "sn": "shona", "sd": "sindhi", "si": "sinhala", "sk": "slovak", "sl": "slovenian", "so": "somali", "es": "spanish", "su": "sundanese", "sw": "swahili", "sv": "swedish", "tg": "tajik", "ta": "tamil", "te": "telugu", "th": "thai", "tr": "turkish", "uk": "ukrainian", "ur": "urdu", "uz": "uzbek", "vi": "vietnamese", "cy": "welsh", "xh": "xhosa", "yi": "yiddish", "yo": "yoruba", "zu": "zulu", "fil": "Filipino", "he": "Hebrew"}

"rg = Recognizer()"

d_l_buttons = 0

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
        myobj.save("speech.mp3")  # Saving the converted audio in an mp3 file
        playsound.playsound("speech.mp3", True)  # Playing the converted file
    except ValueError:
        # Passing the text and language, speed, and accent to gtts
        myobj = gTTS(text=ttk.output, slow=False, lang="en")
        myobj.save("speech.mp3")  # Saving the converted audio in an mp3 file
        playsound.playsound("speech.mp3", True)  # Playing the converted file
    except AssertionError:
        pass

def clear():  # Clear both text boxes
    entry.delete(1.0, "end")
    result.config(text="")


def copy():  # Copy the text
    window.clipboard_clear()
    window.clipboard_append(result["text"])


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
    submit()
    get_info()


def close_history():
    history_win.destroy()


def clear_history():
    with sqlite3.connect("translation_history.db") as db :
        """
           Delete all rows in the tasks table
           :param conn: Connection to the SQLite database
           :return:
           """
        sql = 'DELETE FROM History'
        cur = db.cursor()
        cur.execute(sql)
        db.commit()
        history_win.destroy() #For now
        #Need to figure out how to update tree viewer to show data once cleared

def history_window():
    global history_win
    try:
        history_win.destroy()
    except:
        pass
    history_win = Tk()  # Create the window
    history_win.geometry("1000x500")  # Set the size
    history_win.title("Translation History")  # Set the title
    history_win.resizable(False, False)  # Disable resizing
    history_win.tk.call("source", "azure.tcl")
    history_win.tk.call("set_theme", "dark")
    if d_l_buttons == 1:
        history_win.tk.call("set_theme", "light")

    else:
        history_win.tk.call("set_theme", "dark")

    close_button = ttk.Button(history_win, text="Close", cursor="hand2", style="Accent.TButton", command=close_history)
    close_button.place(x=250, y=450)
    clear_history_b = ttk.Button(history_win, text="Clear History", cursor="hand2", style="Accent.TButton", command=clear_history)
    clear_history_b.place(x=300, y=450)

    def query_database():
        with sqlite3.connect("translation_history.db") as db :
            cursor = db.cursor()

            cursor.execute("SELECT rowid, * FROM History")
            records = cursor.fetchall()

            # Add data to the screen
            global count
            count = 0

            for record in records :
                if count % 2==0 :
                    my_tree.insert(parent='', index='end', iid=count, text='',
                                   values=(record[1], record[2], record[3], record[4]),
                                   tags=('evenrow',))
                else :
                    my_tree.insert(parent='', index='end', iid=count, text='',
                                   values=(record[1], record[2], record[3], record[4]),
                                   tags=('oddrow',))
                # increment counter
                count += 1

            db.commit()

    # Treeview
    style = ttk.Style(history_win)

    # style.configure("Treeview",
    #                 background="#D3D3D3",
    #                 foreground="black",
    #                 rowheight=25,
    #                 fieldbackground="#D3D3D3")
    # style.map("Treeview", backgroun=[("selected", "black")])

    tree_frame = ttk.Frame(history_win)
    tree_frame.pack(pady=10)

    tree_scroll = ttk.Scrollbar(tree_frame)
    tree_scroll.pack(side=RIGHT, fill=Y)

    my_tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set, selectmode="extended")
    my_tree.pack()

    tree_scroll.config(command=my_tree.yview)

    # Define Columns
    my_tree['columns'] = ("Input", "Translation", "Language", "Date")

    # Format Columns
    my_tree.column("#0", width=0, stretch=NO)
    my_tree.column("Input", anchor=W, width=330)
    my_tree.column("Translation", anchor=W, width=330)
    my_tree.column("Language", anchor=CENTER, width=145)
    my_tree.column("Date", anchor=CENTER, width=145)

    # Create Headings
    my_tree.heading("#0", text="", anchor=W)
    my_tree.heading("Input", text="Input", anchor=W, command="sort_id")
    my_tree.heading("Translation", text="Translation", anchor=W, command="sort_name")
    my_tree.heading("Language", text="Language", anchor=CENTER, command="sort_sp")
    my_tree.heading("Date", text="Date", anchor=CENTER, command="sort_pp")

    # Striped Row Tags
    if d_l_buttons == 1:
        my_tree.tag_configure('oddrow', background="#f4f2f2")
        my_tree.tag_configure('evenrow', background="#ffffff")
    else:
        my_tree.tag_configure('evenrow', background="#303030")
        my_tree.tag_configure('oddrow', background="#3f3f3f")

    # connect database
    with sqlite3.connect("translation_history.db") as db :
        cursor = db.cursor()

        cursor.execute("""CREATE TABLE if not exists Product (
                        Input text,
                        Translation text,
                        Language text,
                        Date text)
                        """)

        db.commit()

    query_database()

    history_win.mainloop()



def listen():
    rg.listening()
    rg.paste(entryValue)


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

card = ttk.Frame(window, style='Card.TFrame', padding=(5, 6, 7, 8))
card.place(x=335, y=300)
# Things to do
# Fix up create table code, get history to open new window to display past translation history, make it show
# pre and post translation with language and time/date. Add option to clear database/history
# Make it easy to copy bits you need from history window
# mic func to rishans STT code
# In general make UI look tad nicer

# tempCreate = Button(window, text="Create", command=create_table)
# tempCreate.place(x=355, y=250)

window.mainloop()