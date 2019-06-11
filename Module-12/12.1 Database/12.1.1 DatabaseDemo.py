# database 

import mysql.connector

def createConn():
    print("Create Connection Method Called")
    # connection
    return mysql.connector.connect(host="localhost",database="python",user="root",password="",port=3306)

def insertdata(fname,lname,email):
    print("Insert Method Called")
    query="insert into student(fname,lname,email)values(%s,%s,%s)" # insert data 
    args=(fname,lname,email)
    conn = createConn()
    cursor=conn.cursor()
    cursor.execute(query,args)
    conn.commit()
    print("data Successfully insert")
    

f=input("Enter the fname : ")
l=input("Enter the lname : ")
e=input("Enter the email : ")
insertdata(f, l, e)