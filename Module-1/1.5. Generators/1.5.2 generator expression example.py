# Generator expression to generate squares of numbers
squares = (x**2 for x in range(5))


# Iterating over the generator
for square in squares:
    print(square)
