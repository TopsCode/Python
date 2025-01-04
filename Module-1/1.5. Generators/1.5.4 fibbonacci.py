def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        yield a
        a, b = b, a + b

# Create the Fibonacci generator
fib = fibonacci(5)

# Iterate and print the Fibonacci numbers
for num in fib:
    print(num)
