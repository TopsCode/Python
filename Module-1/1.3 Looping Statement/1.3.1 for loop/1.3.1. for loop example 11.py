# accept 5 numbers from user and perform addition 

sum = 0 
for i in range(1,6):
    num = int(input("Enter a number : "))
    sum += num 

print(f"sum = {sum}")