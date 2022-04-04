from tkinter import *
from tkinter import ttk
import sqlite3


d_l_buttons = 0


def create_history_window():
    history_win = Tk()  # Create the window
    history_win.geometry("1000x400")  # Set the size
    history_win.title("Translation History")  # Set the title
    history_win.resizable(False, False)  # Disable resizing
    history_win.tk.call("source", "azure.tcl")
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

    copy_dark = PhotoImage(file="copy-d.png")
    copy_light = PhotoImage(file="copy-l.png")

    copy_button_1 = Button(history_win, image=copy_dark, bd=0, cursor="hand2", command=copy_1)
    copy_button_1.place(x=820, y=330)
    # Make these copy buttons change form light/dark once linked with main py
    copy_button_2 = Button(history_win, image=copy_dark, bd=0, cursor="hand2", command=copy_2)
    copy_button_2.place(x=820, y=365)

    # Add History to treeview
    query_database()

    # Bindings
    my_tree.bind("<Double-1>", select_record)
    input_box.bind("<1>", lambda e: input_box.focus_set())
    translation_box.bind("<1>", lambda e: translation_box.focus_set())

    history_win.mainloop()
