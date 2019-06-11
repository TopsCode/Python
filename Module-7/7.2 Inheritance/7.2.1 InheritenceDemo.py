# inheritance example
class Person():
    fname=""
    lname=""
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
    def showName(self):
        print("First Name : ",self.fname," And Last Name : ",self.lname)

class Employee(Person):
    
    sno=0
    def __init__(self,fname,lname,sno):
        Person.__init__(self, fname, lname)
        self.sno=sno
        
    def showEmployee(self):
        self.showName()
        print("Staff Number : ",self.sno)

b=Person("Sunit","Jha")
a=Employee("Sunit","Jha",8)
#b.showName()
a.showEmployee()