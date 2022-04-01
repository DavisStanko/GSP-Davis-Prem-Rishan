from tkinter import *
from tkinter import ttk, messagebox, filedialog
import sqlite3
import csv
import os

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


# Treeview
style = ttk.Style()
style.theme_use("default")

history_win.tk.call("source", "azure.tcl")
history_win.tk.call("set_theme", "dark")

# style.configure("Treeview",
#                 background="#D3D3D3",
#                 foreground="black",
#                 rowheight=25,
#                 fieldbackground="#D3D3D3")
# style.map("Treeview", backgroun=[("selected", "black")])

tree_frame = Frame(history_win)
tree_frame.pack(pady=10)

tree_scroll = Scrollbar(tree_frame)
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
my_tree.tag_configure('oddrow', background="whitesmoke")
my_tree.tag_configure('evenrow', background="white")

# connect database
with sqlite3.connect("translation_history.db") as db:
    cursor = db.cursor()

    cursor.execute("""CREATE TABLE if not exists Product (
                    Input text,
                    Translation text,
                    Language text,
                    Date text)
                    """)

    db.commit()

close_button = ttk.Button(history_win, text="Close", cursor="hand2", style="Accent.TButton", command="close_history")
close_button.place(x=250, y=350)

# Add History to treeview
query_database()

history_win.mainloop()
