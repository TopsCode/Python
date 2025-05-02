session = {
    'is_loggin' : False,
    "email" : ""
}

valid_email = "test@gmail.com"
valid_password = "123456"

def login():
    email = input("ENter your email : ")
    password = input("Enter your password : ")

    if email == valid_email and password == valid_password:
        session["is_loggin"] = True
        session["email"] = email

        print("Successfully logged in !! ")
    else:
        print("invalid credentials !!!")


def login_validation(myfun):
    def wrapperFun():
        if session["is_loggin"]:
            myfun()
        else:
            print("ACCESS DENIED !!! Please login first !!!")
    return wrapperFun

@login_validation
def profile():
    print("WELCOME TO PROFILE PAGE :: ")

@login_validation
def account():
    print("ACCOUNT PART IS HERE NO DUE IS HERE .... ")
    
@login_validation
def logout():
    session["is_loggin"] = False
    session["email"]  = ""

    print("Successfully Logout !!!")


status = True
while status:

    menu = """ 
                    1) Login
                    2) Profile 
                    3) Account 
                    4) Logout
        """

    print(menu)

    choice = int(input("Enter your choice : "))

    if choice == 1:
        login() 
    elif choice == 2:
        profile()
    elif choice == 3:
        account()
    elif choice == 4:
        logout()
        

