# exception demo 

from builtins import int
while True:
    try:
        n=input("Enter the value : ")
        n=int(n)
        break
    except Exception:
        print("Invalid Input")
    finally:
        print("Finally Called")
print("Bye")