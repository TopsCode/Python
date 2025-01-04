l1 = [23,34,54,67,34]

def checkEven(num):
    if num%2 == 0:
        return "Even" 
    else:
        return "Odd"
    
l2 = list(map(checkEven,l1))
print(l2)

