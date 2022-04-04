# import tkinter as tk
# my_w = tk.Tk()
# my_w.geometry("400x300")
# l1 = tk.Label(my_w,text='Your Name', width=10) #added one Label
# l1.grid(row=1,column=1)
# my_wrap=tk.StringVar(value='none')
# t1 = tk.Text(my_w,width=15,height=4,bg='yellow',wrap=my_wrap.get())
# t1.grid(row=1,column=2)
# def my_fun():
#     if(t1['wrap']=='word'):
#         t1.config(wrap='none')
#     else:
#         t1.config(wrap='word')
#     #print(t1['wrap'])
# menubar = tk.Menu(my_w)
# menu_file = tk.Menu(menubar, tearoff=0,bg='yellow') # file
# menu_edit=tk.Menu(menubar,tearoff=0)  # edit menu
# menubar.add_cascade(label="File", menu=menu_file) # Top Line
# menu_file.add_checkbutton(label='Wrap',command=lambda:my_fun())
# my_w.config(menu=menubar) # adding menu to window
# my_w.mainloop()

import tkinter as tk
my_w = tk.Tk()
my_w.geometry("400x300")

# my_wrap=tk.StringVar(value='none')
t1 = tk.Text(my_w,width=15,height=4,bg='black',wrap='word')
t1.pack()


my_w.mainloop()