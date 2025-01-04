numbers = [1, 2, 3, 4, 5]

# Using lambda to square each number
squared_numbers = map(lambda x: x ** 2, numbers)

print(list(squared_numbers))  # Output: [1, 4, 9, 16, 25]
