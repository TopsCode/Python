import pymysql
mydb = pymysql.connect(host="localhost",user="root",password="",port=3307,database="topsdb")
mycursor = mydb.cursor() 

menu = """
                menu 

            1) add students 
            2) view students 
            3) search student 
            4) update student 
            5) delete student 

"""

def add_student():
    name = input("Enter your name : ")
    subject = input("Enter your subject : ")

    args = (name,subject)
    query = "insert into student (name,subject) values ('%s','%s') "

    mycursor.execute(query%args)

    mydb.commit()

    print("successfully record inserted !!!")

def view_student():
    query = "select * from student "

    mycursor.execute(query)

    result = mycursor.fetchall() 

    print(result)

    for stu in result:
        print("name : ",stu[1])

def search_student():
    name = input("Enter student name which you want to search : ")
    args = (name)
    query = "select * from student where name = '%s' "
    mycursor.execute(query%args)

    result = mycursor.fetchone() 

    print("id : ",result[0])
    print("name : ",result[1])
    print("subject : ",result[2])

    mydb.commit()

status = True
while status:
    print(menu)
    user_choice = int(input("which option you want to go for it : "))   
    if user_choice == 1:
        add_student() 
    elif user_choice == 2:
        view_student() 
    elif user_choice == 3:
        search_student() 
