from tkinter import * 
from PIL import Image,ImageTk


screen = Tk() 
screen.geometry("350x350")
screen.title("IMAGE")

image = Image.open("pizza.png")
image = image.resize((150,150)) # width , height

photo = ImageTk.PhotoImage(image)

lbl = Label(screen,image=photo,bd=10)
lbl.pack()

screen.mainloop()