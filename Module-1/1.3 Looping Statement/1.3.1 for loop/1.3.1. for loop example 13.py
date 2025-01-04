# accept 5 marks from user and perform addition of above 70 score 

sum = 0 

for i in range(1,6):
    marks = int(input("Enter marks : "))
    if marks > 70:
        sum += marks 

print(sum)