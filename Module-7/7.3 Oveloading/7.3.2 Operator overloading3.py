# operator overloading

class Point:
   def __init__(self, x,y):
       self.x=x
       self.y=y

   def __str__(self):
       return "({0},{1})".format(self.x,self.y)

   def __add__(self,other):
       x=self.x + other.x
       y=self.y + other.y
       return Point(x,y)

p1=Point(10,20)
p2=Point(5,4)
print("Addition of two points ",p1+p2)
