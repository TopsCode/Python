class Calculator:
    
    @staticmethod
    def add(x, y):
        return x + y
    
    @staticmethod
    def multiply(x, y):
        return x * y

# Calling static methods
print(Calculator.add(5, 3))      # Output: 8
print(Calculator.multiply(5, 3)) # Output: 15
