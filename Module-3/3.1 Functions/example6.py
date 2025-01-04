def findFactorial():
    fact = 1
    num = int(input("Enter a number : "))
    for i in range(1,num+1):
        fact *= i 
    return fact

print(f"factorial = {findFactorial()}")

