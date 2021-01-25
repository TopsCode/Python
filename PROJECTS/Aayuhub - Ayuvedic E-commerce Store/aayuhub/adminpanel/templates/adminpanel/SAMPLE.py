from tkinter import * 
import tkinter.scrolledtext as ScrolledText
import tkinter.filedialog as filedialog
import os
import tkinter.messagebox as messagebox

window=Tk()
window.geometry("500x500")
window.title("Notepad")

def openfile():
    file=filedialog.askopenfile(parent=window,title="open",filetypes=(("Text Files","*.txt"),("All Files","*.*")))

    window.title(os.path.basename(file.name)+"- Notepad")
    if file!=None:
        content=file.read()
        textarea.insert('1.0',content)
        file.close()

def savefile():
    file=filedialog.asksaveasfile(mode='w')
    if file!=None:
        data=textarea.get('1.0',END+'-1c')
        file.write(data)
        file.close()

def exitFile():
    if messagebox.askyesno("Exit","Are you sure you want to exit ?"):
        window.destroy()

def newFile():
    if len(textarea.get('1.0',END+'-1c'))>0:
        if messagebox.askyesno("Save File","Do you want to save this file ?"):
            savefile()
        else:
            textarea.delete('1.0',END)

textarea=ScrolledText.ScrolledText(window,height=500,width=500)
textarea.pack()


menubar=Menu(window)
window.config(menu=menubar)

filemenu=Menu(menubar,tearoff=0)
aboutmenu=Menu(menubar,tearoff=0)

menubar.add_cascade(label="File",menu=filemenu)
menubar.add_cascade(label="About",menu=aboutmenu)

filemenu.add_command(label="New",command=newFile)
filemenu.add_command(label="Open",command=openfile)
filemenu.add_command(label="Save",command=savefile)

filemenu.add_separator()

filemenu.add_command(label="Exit",command=exitFile)

window.mainloop()