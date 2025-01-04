# Add corresponding elements from two lists
numbers1 = [1, 2, 3, 4]
numbers2 = [5, 6, 7, 8]

# Using lambda to add corresponding elements
sum_of_numbers = map(lambda x, y: x + y, numbers1, numbers2)

print(list(sum_of_numbers))  # Output: [6, 8, 10, 12]
