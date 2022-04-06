from tkinter import *  # GUI
import tkinter.ttk as ttk  # Themes
from gtts import gTTS  # Google text to speech
from deep_translator import GoogleTranslator  # Google Translator
import playsound  # Play speech
import sqlite3  # Storing past translations
import datetime  # Getting date of translation

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

##################################

start_value = 0

speaking_txt = 0


def startup():
    global rg
    rg = None

    if start_value == 1:
        from speech_recog import Recognizer
        rg = Recognizer()


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
    global speaking_txt
    lang = get_key(option_variable.get())  # Get the output language
    ttk.output = GoogleTranslator(source="auto", target=lang).translate(entry.get(1.0, "end"))  # Translate the text
    result.config(text=ttk.output)
    if speaking_txt == 1:
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
    else:
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


def history_window():
    create_history_window()


def enable_mic():
    global start_value

    start_value = 1
    mic_button.place(x=335, y=300)


def listen():
    global start_value, mic_value
    mic_value = True
    mic_enabled()

    start_value = 1
    startup()

    entry.delete(1.0, "end")
    result.config(text="")

    rg.listening()
    detected = rg.paste(entryValue)
    entry.insert(END, detected)

    mic_value = False


def mic_enabled():
    global mic_value

    if mic_value:
        mic_button.config(image=mic_enable)
    else:
        pass


def help_option():
    global d_l_buttons

    help_win = Tk()  # Create the window
    help_win.geometry("430x400")  # Set the size
    help_win.title("Help")  # Set the title
    help_win.resizable(False, False)  # Disable resizing
    help_win.tk.call("source", "data/azure.tcl")
    help_win.tk.call("set_theme", "dark")

    if d_l_buttons == 1:
        help_win.tk.call("set_theme", "light")

    else:
        help_win.tk.call("set_theme", "dark")


    main_frame = ttk.Frame(help_win)
    main_frame.pack(fill=BOTH, expand=1)

    my_canvas = Canvas(main_frame)
    my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

    help_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
    help_scrollbar.pack(side=RIGHT, fill=Y)

    my_canvas.configure(yscrollcommand=help_scrollbar.set)
    my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))

    second_frame = ttk.Frame(my_canvas)

    my_canvas.create_window((0, 0), window=second_frame, anchor=NW)

    instructions = ttk.Label(second_frame, text="Instructions", font=('Apple', 24, "underline"))
    instructions.pack(side=TOP, anchor=NW, padx=10, pady=10)

    instruct_text = "‣  Input the text to be translated in the designated field.\n" \
                    '\n   ‣  The language will be detected automatically.\n' \
                    '\n‣  Select the output language from the drop down menu.\n' \
                    '\n‣  Click the submit button when ready.\n'

    instruct_cont = ttk.Label(second_frame, text=instruct_text, font=('Apple', 16), justify=LEFT, wraplength=385)
    instruct_cont.pack(anchor=W, padx=10)

    speech_label = ttk.Label(second_frame, text="How to Use Speech-to-Text", font=('Apple', 24, "underline"))
    speech_label.pack(side=TOP, anchor=NW, padx=10, pady=10)

    instruct2_text = "‣  Options > Enable Mic\n" \
                     '\n‣  The mic image will appear in the center of the program.\n' \
                     '\n‣  Hit the button and speak clearly.\n' \
                     '\n   ‣  The mic will turn green to show it is working.\n'

    instruct2_cont = ttk.Label(second_frame, text=instruct2_text, font=('Apple', 16), justify=LEFT, wraplength=385)
    instruct2_cont.pack(anchor=W, padx=10)


##################################

window = Tk()  # Create the window
window.geometry("700x500")  # Set the size
window.title("Translate")  # Set the title
window.resizable(False, False)  # Disable resizing

# Dark/Light mode toggle
dark_mode = True
on = PhotoImage(file="data/dark.png")
off = PhotoImage(file="data/light.png")
onButton = Button(window, image=on, bd=0, cursor="hand2", command=switch)
onButton.place(x=630, y=25)

# Default theme
window.tk.call("source", "data/azure.tcl")
window.tk.call("set_theme", "dark")

# Title
labelTittle = ttk.Label(window, text="Translator",
                        font=("Apple", 32, "bold"), borderwidth=10, relief=GROOVE, background="#2c73e6")
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

copy_dark = PhotoImage(file="data/copy-d.png")
copy_light = PhotoImage(file="data/copy-l.png")

copy = Button(window, image=copy_dark, bd=0, cursor="hand2", command=copy)
copy.place(x=335, y=350)

history_dark = PhotoImage(file="data/history-d.png")
history_light = PhotoImage(file="data/history-l.png")

history = Button(window, image=history_dark, bd=0, cursor="hand2", command=history_window)
history.place(x=335, y=250)

mic_dark = PhotoImage(file="data/mic-d.png")
mic_light = PhotoImage(file="data/mic-l.png")
mic_enable = PhotoImage(file="data/mic-green.png")

mic_value = False
mic_button = Button(window, image=mic_dark, bd=0, cursor="hand2", command=listen)

# Menu

def speaking_enable():
    global speaking_txt
    speaking_txt = 1

def speaking_disable():
    global speaking_txt
    speaking_txt = 0

upper_menu = Menu(window)
window.config(menu=upper_menu)
options_menu = Menu(upper_menu)
upper_menu.add_cascade(label="Options", menu=options_menu)
options_menu.add_command(label="Enable Mic", command=enable_mic)
options_menu.add_command(label="Enable Speech", command=speaking_enable)
options_menu.add_command(label="Disable Speech", command=speaking_disable)
options_menu.add_command(label="Help", command=help_option)




def create_history_window():
    global d_l_buttons

    history_win = Tk()  # Create the window
    history_win.geometry("1000x400")  # Set the size
    history_win.title("Translation History")  # Set the title
    history_win.resizable(False, False)  # Disable resizing
    history_win.tk.call("source", "data/azure.tcl")
    history_win.tk.call("set_theme", "dark")

    def query_database():
        with sqlite3.connect("translation_history.db") as db:
            cursor = db.cursor()

            cursor.execute("SELECT rowid, * FROM History")
            records = cursor.fetchall()

            # Add data to the screen
            global count
            count = 0

            for record in records:
                if count % 2 == 0:
                    my_tree.insert(parent='', index='end', iid=count, text='',
                                   values=(record[1], record[2], record[3], record[4]),
                                   tags=('evenrow',))
                else:
                    my_tree.insert(parent='', index='end', iid=count, text='',
                                   values=(record[1], record[2], record[3], record[4]),
                                   tags=('oddrow',))
                # increment counter
                count += 1

            db.commit()

    def update_treeview(records):
        my_tree.delete(*my_tree.get_children())

        with sqlite3.connect("translation_history.db") as db:
            cursor = db.cursor()
            cursor.execute("SELECT rowid, * FROM History")

            for item in records:
                my_tree.insert("", 'end', iid=item[0], text=item[0],
                               values=(item[1], item[2], item[3], item[4]))
                db.commit()

    def clear_entries():
        input_box.delete(0, END)
        translation_box.delete(0, END)

    def select_record(e):
        try:
            # Clear entry boxes
            clear_entries()

            # Grab record Number
            selected = my_tree.focus()
            # Grab record values
            values = my_tree.item(selected, 'values')

            # Make entries able to edit
            input_box.config(state=NORMAL)
            translation_box.config(state=NORMAL)

            # Outputs to entry boxes
            input_box.insert(0, values[0])
            translation_box.insert(0, values[1])

            """# Make entries unable to edit
            input_box.config(state=DISABLED)
            translation_box.config(state=DISABLED)"""

        except IndexError:
            pass

    def clear_history():
        with sqlite3.connect("translation_history.db") as db:
            """
               Delete all rows in the tasks table
               :param conn: Connection to the SQLite database
               :return:
               """
            sql = 'DELETE FROM History'
            cur = db.cursor()
            cur.execute(sql)

            records = cur.fetchall()
            update_treeview(records)
            db.commit()

    def close_history():
        history_win.destroy()

    def copy_1():
        history_win.clipboard_clear()
        history_win.clipboard_append(input_box.get())
        history_win.update()

    def copy_2():
        history_win.clipboard_clear()
        history_win.clipboard_append(translation_box.get())
        history_win.update()

    copy_dark = PhotoImage(master=history_win, file="data/copy-d.png")
    copy_light = PhotoImage(master=history_win, file="data/copy-l.png")

    copy_button_1 = Button(history_win, image=copy_dark, bd=0, cursor="hand2", command=copy_1)
    copy_button_1.place(x=820, y=330)
    # Make these copy buttons change form light/dark once linked with main py
    copy_button_2 = Button(history_win, image=copy_dark, bd=0, cursor="hand2", command=copy_2)
    copy_button_2.place(x=820, y=365)

    if d_l_buttons == 1:
        history_win.tk.call("set_theme", "light")
        copy_button_1.config(image=copy_light)
        copy_button_2.config(image=copy_light)
    else:
        history_win.tk.call("set_theme", "dark")
        copy_button_1.config(image=copy_dark)
        copy_button_2.config(image=copy_dark)

    # Treeview
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
    with sqlite3.connect("translation_history.db") as db:
        cursor = db.cursor()

        cursor.execute("""CREATE TABLE if not exists History (
                        Input text,
                        Translation text,
                        Language text,
                        Date text)
                        """)

        db.commit()

    # Entry boxes
    input_value = StringVar()
    translation_value = StringVar()

    # Input + Translation data
    input_box = ttk.Entry(history_win, textvariable=input_value, state=DISABLED, width=100)
    input_box.place(x=100, y=330)

    translation_box = ttk.Entry(history_win, textvariable=translation_value, state=DISABLED, width=100)
    translation_box.place(x=100, y=365)

    # Widgets
    close_button = ttk.Button(history_win, text="Close", cursor="hand2", style="Accent.TButton", command=close_history)
    close_button.place(x=400, y=290)

    clear_button = ttk.Button(history_win, text="Clear History", cursor="hand2", style="Accent.TButton",
                              command=clear_history)
    clear_button.place(x=500, y=290)

    # Add History to treeview
    query_database()

    # Bindings
    my_tree.bind("<Double-1>", select_record)
    input_box.bind("<1>", lambda e: input_box.focus_set())
    translation_box.bind("<1>", lambda e: translation_box.focus_set())

    history_win.mainloop()


startup()

window.mainloop()
