# accept 5 marks from user and display above 70 marks as A grade and below 70 as B grade 

for i in range(1,6):
    marks = int(input("Enter marks : "))
    if marks > 70:
        print("A grade")
    else:
        print("B grade")
        