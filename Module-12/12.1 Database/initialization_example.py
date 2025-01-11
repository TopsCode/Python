# need to install database 3rd party library 

# pip : python index package 

import pymysql

mydb = pymysql.connect(host="localhost",user="root",password="",port=3307)

mycursor = mydb.cursor() 

mycursor.execute("create database if not exists topsdb")

mydb.commit()  # save 

mydb = pymysql.connect(host="localhost",user="root",password="",port=3307,database="topsdb")

mycursor = mydb.cursor()

mycursor.execute("create table student (id int primary key auto_increment , name varchar(20),subject varchar(20)) ")

mydb.commit()


