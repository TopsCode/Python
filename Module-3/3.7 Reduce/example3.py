from functools import reduce

# Function to add two numbers
def add(x, y):
    return x + y

numbers = [1, 2, 3, 4]
result = reduce(add, numbers, 100)  # 100 is the initializer
print(result)  # Output: 110
