def findFactorial():
    f = 1
    num = int(input("Enter a number : "))
    for i in range(1,num+1):
        f*=i
    print(f)


findFactorial()  