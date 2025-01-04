def checkEvenOdd(num): # function with arguments and function return type 
    if num%2==0:
        return "even"
    else:
        return "odd"


number = int(input("Enter a number : "))
print(checkEvenOdd(number))