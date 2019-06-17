import mysql.connector

def createConn():
    print("Create Connection Method Called")
    # connection
    return mysql.connector.connect(host="localhost",database="python_demo",user="root",password="password",port=3306)

def deletedata():
    conn = createConn()
    cursor=conn.cursor()
    sql = "DELETE FROM student WHERE email = 'aa@gmail.com'"
    cursor.execute(sql)
    conn.commit()
    print(cursor.rowcount, "record(s) affected")

deletedata()