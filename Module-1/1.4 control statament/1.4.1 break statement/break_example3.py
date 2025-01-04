# accept marks from user and check if marks below 35 terminate process

for i in range(1,6):
    marks = int(input("Enter marks : "))
    if marks < 35:
        break

    print("marks : ",marks)