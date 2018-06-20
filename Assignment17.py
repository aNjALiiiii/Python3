#QUES1 Write a python program using tkinter interface to write Hello World and a exit button that closes the interface.
#and
#Ques2  Write a python program to in the same interface as above and create a action when the button is click
# it will display some text.
import tkinter as tk
from tkinter import *
def write_hello():
    print("Hello World")
    w.configure(text="hello world")
root = tk.Tk(className="title")
frame = tk.Frame(root)
l = Label(root,text="Welcome")
l.pack(side=TOP)
w=Label(root,text="")
w.pack(side=tk.BOTTOM)
frame.pack()
button = tk.Button(frame,
                   text="QUIT",
                   fg="red",
                   command=quit)
button.pack(side=tk.LEFT)
text_button = tk.Button(frame,
                   text="text",
                   command=write_hello)
text_button.pack(side=tk.LEFT)

root.mainloop()


#Ques3 Create a frame using tkinter with any label text and two buttons.One to exit
#and other to change the label to some other text.
def change_lable():
    w.configure(text="its fun")
root = tk.Tk(className="title")
frame1 = tk.Frame(root)
w=Label(root,text="")
w.pack(side=tk.BOTTOM)
frame1.pack()
button = tk.Button(frame1,
                   text="QUIT",
                   fg="red",
                   command=quit)
button.pack(side=tk.LEFT)
text_button = tk.Button(frame1,
                   text="change",
                   command=change_lable)
text_button.pack(side=tk.LEFT)
root.mainloop()


#Ques4 Write a python program using tkinter interface to take an input in the GUI program and print it.
def show_entry_fields():
   print("First Name: %s\nLast Name: %s" % (e1.get(), e2.get()))
   label3.configure(text="Welcome "+e1.get()+" "+e2.get())
master = Tk()
Label(master, text="First Name").grid(row=0)
Label(master, text="Last Name").grid(row=1)

e1 = Entry(master)
e2 = Entry(master)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

Button(master, text='Quit', command=master.quit).grid(row=3, column=0, sticky=W, pady=4)
Button(master, text='Show', command=show_entry_fields).grid(row=3, column=1, sticky=W, pady=4)
label3=Label(master,text="")
label3.grid(row=4,column=4)

mainloop( )
