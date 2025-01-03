# accept 5 numbers from user and check entered number is even or odd 

"""
output : Enter a number : 12
        Even number 
         Enter a number : 3
        Odd number 
"""

for i in range(1,6):
    num = int(input("Enter a number : "))
    if num%2 == 0:
        print("Even number")
    else:
        print("odd number")
    