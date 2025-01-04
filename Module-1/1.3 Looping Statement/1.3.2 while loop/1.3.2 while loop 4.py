# accept name until user enter no 

status = True 
while status:
    name = input("Enter your name : ")
    choice = input("Do you want to continue press y for yes and press n for no : ").lower() 
    if choice == 'y' or choice == 'yes':
        status = True 

    else:
        status = False 

