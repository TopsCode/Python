# exception demo 

a= int(input("Enter the value of A :"))
b= int(input("Enter the value of B :"))

try:
    c=a/b 
    print("Division : ",c)
except Exception:
    print("Execption Caught")
    
    
print("Bye")
