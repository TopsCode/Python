# function without parameters and function without return type 
def menu():
    menuItem = """
                        MENU 

                    press 1 for addition 
                    press 2 for multiplication 
                    press 3 for substraction 
                    press 4 for division 
        """
    print(menuItem)

def addition():
    num1 = int(input("Enter number 1 : "))
    num2 = int(input("Enter number 2 : "))

    ans = num1 + num2 
    print(ans)

def multiplication():
    num1 = int(input("Enter number 1 : "))
    num2 = int(input("Enter number 2 : "))

    ans = num1 * num2 
    print(ans)


menu() 
choice = int(input("Enter your choice : "))
if choice == 1:
    addition() 
elif choice == 2:
    multiplication() 