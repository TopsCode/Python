numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Use lambda to filter odd numbers
odd_numbers = filter(lambda x: x % 2 != 0, numbers)

# Convert to list and print the result
print(list(odd_numbers))  # Output: [1, 3, 5, 7, 9]
