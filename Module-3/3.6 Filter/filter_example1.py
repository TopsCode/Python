l1 = [23,34,45,67,23,98]

def checkEven(num):
    if num%2 == 0:
        return num 


l2 = list(filter(checkEven,l1))
print(l2)