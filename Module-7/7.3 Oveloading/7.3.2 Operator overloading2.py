# __add__ automatically invoked  (+) operator is defined 


class Sample:
   def __init__(self,a):
       self.a=a
   def __add__(self,b):
       return self.a+b.a

obj1=Sample(5)
obj2=Sample(10)
obj3=Sample("Python")
obj4=Sample("Programming ")

print(obj1+obj2)
print(obj3+obj4)
