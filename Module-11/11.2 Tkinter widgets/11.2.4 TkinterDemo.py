# Tkinter example

from tkinter import *

master=Tk()
Label(master, text="First Name").grid(row=0)
Label(master, text="Last Name").grid(row=1)
Label(master, text="Email").grid(row=2)
Label(master, text="Mobile").grid(row=3)
Label(master, text="Hobby").grid(row=4)

e1 = Entry(master)
e2 = Entry(master)
e3 = Entry(master)
e4 = Entry(master)

e1.grid(row=0, column=5)
e2.grid(row=1, column=5)
e3.grid(row=2, column=5)
e4.grid(row=3, column=5)

var1 = IntVar()
Checkbutton(master, text="Music", variable=var1).grid(row=4, column=5)
print(var1.get())
var2 = IntVar()
Checkbutton(master, text="Travelling", variable=var2).grid(row=5, column=5)

b1=Button(master, text='Insert Data').grid(row=6,column=1)
master.mainloop()