import mysql.connector

def createConn():
    print("Create Connection Method Called")
    # connection
    return mysql.connector.connect(host="localhost",database="python_demo",user="root",password="password",port=3306)

def createTable():
    conn = createConn()
    cursor=conn.cursor()
    cursor.execute
    cursor.execute("CREATE TABLE student (fname VARCHAR(255),lname VARCHAR(255),email VARCHAR(255))")
        
createTable()