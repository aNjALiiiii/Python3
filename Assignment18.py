'''Q1. Create a dict with name and mobile number.
 Define a GUI interface using tkinter and pack the label and create a scrollbar to
 scroll the list of keys in the dictionary.
And---->
Ques2 In the same tkinter file as created above, create a function to insert items into the dictionary.'''
from tkinter import *

root = Tk()
label=Label(root,text=" PHONEBOOK : ")
label.pack()
phone={"ab":"0123456789","cd":"9874563210"}

def add():
    phone.update({x.get():y.get()})
    for key in phone.keys():
        print(key)
    i=key
    listbox.insert(END, i)

scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

listbox = Listbox(root)
listbox.pack()

for i in phone.keys():
    listbox.insert(END, i)

# attach listbox to scrollbar
listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)
label1 = Label(root,text="Wanna add a new no?\nEnter Name and Number")
label1.pack()
label2 = Label(root,text="Name")
x = Entry(root,text="Name")
y=Entry(root,text="Phone no")
x.pack()
y.pack()
button = Button(text="Enter",command=add)
button.pack()
mainloop()