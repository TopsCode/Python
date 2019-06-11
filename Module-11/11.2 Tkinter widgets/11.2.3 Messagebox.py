# using of messagebox

from tkinter import * 
from tkinter import messagebox

window = Tk() 
window.geometry("200x100") 
def fun(): 
   messagebox.showinfo("Hello", "WELCOME TO TKINTER") 
b1 = Button(window,text = "SUBMIT ",command = fun)
b1.pack() 
window.mainloop() 

