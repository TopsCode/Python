# tkinter with widgets

from tkinter import *

window=Tk()
window.title("My APP")
window.geometry("250x250")
b= Button(window,text="First Button")
b.pack()
window.mainloop()
