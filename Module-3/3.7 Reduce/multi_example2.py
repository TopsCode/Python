from functools import reduce

# Function to multiply two numbers
def multiply(x, y):
    return x * y

numbers = [1, 2, 3, 4, 5]
result = reduce(multiply, numbers)
print(result)  # Output: 120
