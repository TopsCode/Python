status = True  # initlization 

while status:
    num = int(input("Enter a number : "))

    choice = input("Do you want to continue press 'y' for yes and press 'n' for no : ").lower()
    if choice == 'y':
        status = True 
    else:
        status = False

