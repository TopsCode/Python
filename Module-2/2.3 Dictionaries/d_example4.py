# store multiple keys and values in a dicitionary 

d = {}

status = True 
while status:
    key = input("Enter your key : ")
    value = input("Enter your value : ")

    d[key] = value
    print(d)
    choice = input("Do you want to add more record : ")
    if choice == 'n':
        status = False

    