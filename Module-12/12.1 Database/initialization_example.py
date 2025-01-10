# need to install database 3rd party library 

# pip : python index package 

import pymysql


mydb = pymysql.connect(host="localhost",user="root",password="",port=3306)

mycursor = mydb.cursor() 

mycursor.execute("create database Student")

mydb.commit()  # save 



