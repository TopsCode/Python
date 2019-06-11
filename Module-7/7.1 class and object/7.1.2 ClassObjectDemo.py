#class and object 

class Person:
    
    fname =""
    lname =""
    email =""
    
    
    def __init__(self,fname,lname,email):
        
        print("Constructor Called")
        self.fname = fname
        self.lname = lname
        self.email = email
    
    def showDetails(self):
        print("Fname :",self.fname)
        print("Lname :",self.lname)
        print("Email :",self.email)

fname = print(input("Enter the Fname :"))
lname = print(input("Enter the Lname :"))
email = print(input("Enter the Email : "))        
p = Person(fname,lname,email)
p.showDetails()