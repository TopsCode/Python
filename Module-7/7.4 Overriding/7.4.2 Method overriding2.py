class Shape:
    def area(self):
        raise NotImplementedError("Subclass must implement this method")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius * self.radius

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

# Creating instances of the subclasses
shapes = [Circle(5), Rectangle(4, 6)]

# Using polymorphism to call the same method on different types of objects
for shape in shapes:
    print(f"Area: {shape.area()}")
