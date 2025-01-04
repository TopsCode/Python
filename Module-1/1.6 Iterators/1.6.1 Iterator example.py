# Creating an iterator from a list
numbers = [1, 2, 3]
iterator = iter(numbers)

print(next(iterator))  # Output: 1
print(next(iterator))  # Output: 2
print(next(iterator))  # Output: 3
print(next(iterator))  # Raises StopIteration
