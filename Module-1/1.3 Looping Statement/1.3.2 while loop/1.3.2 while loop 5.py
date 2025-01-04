sum = 0 

flag = True 
while flag:
    num = int(input("Enter a number : "))
    sum += num 

    choice = input("Do you want to enter more number press n for no : ").lower() 

    if choice == 'n' or choice == 'no':
        flag = False
        print("sum = ",sum)
    


