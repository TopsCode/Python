numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]

# Multiply corresponding elements
products = map(lambda x, y: x * y, numbers1, numbers2)

print(list(products))  # Output: [4, 10, 18]
