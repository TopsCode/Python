# tkinter with widget practical

from tkinter import *
import mysql.connector

def create_conection():
    return mysql.connector.connect(host="localhost",user="root",password="",database="tkinter")
def insert_data(f,l,e,m,v1):
    conn=create_conection()
    cursor=conn.cursor()
    args=(f,l,e,m,v1)
    query="insert into student(fname,lname,email,mobile,hobby) values(%s,%s,%s,%s,%s)"
    cursor.execute(query,args)
    conn.commit()
    print("Data Inserted Successfully")
    conn.close()

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


e1.grid(row=0,column=5)
e2.grid(row=1, column=5)
e3.grid(row=2, column=5)
e4.grid(row=3, column=5)

var1 = IntVar()
Checkbutton(master, text="Music", variable=var1).grid(row=4, column=5)
print(var1.get())
var2 = IntVar()
Checkbutton(master, text="Travelling", variable=var2).grid(row=5, column=5)

b1=Button(master, text='Insert Data',
          command=lambda:insert_data(e1.get(),e2.get(),e3.get(),e4.get(),var1.get())).grid(row=6, column=1)
master.mainloop()