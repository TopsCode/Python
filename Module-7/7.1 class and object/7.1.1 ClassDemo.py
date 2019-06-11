# class and object practical 

class MyClass:
    
    x = 0
    def __init__(self,x):
        self.x=x 
    
    def my_method(self):
        print("X:",self.x)
    
    
    def OddEven(self):
        if self.x%2==0:
            print(self.x,"Is even number")
        else:
            print(self.x,"Is Odd number")
            
x=int(input("enter the value of X :"))

a=MyClass(x)
a.my_method()
a.OddEven()