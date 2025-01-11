class Rectangle:
    def __init__(self, *args):
        if len(args) == 0:
            self.width = 0
            self.height = 0
        elif len(args) == 1:
            self.width = args[0]
            self.height = args[0]  # Square case
        elif len(args) == 2:
            self.width = args[0]
            self.height = args[1]

    def display(self):
        print(f"Width: {self.width}, Height: {self.height}")

# Creating Rectangle objects in different ways
r1 = Rectangle()  # Default rectangle (0x0)
r2 = Rectangle(5)  # Square (5x5)
r3 = Rectangle(4, 6)  # Rectangle (4x6)

r1.display()  # Output: Width: 0, Height: 0
r2.display()  # Output: Width: 5, Height: 5
r3.display()  # Output: Width: 4, Height: 6
