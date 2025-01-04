"""
yield: Instead of returning a value, the yield statement 
pauses the function and sends a value back to the caller.

When the generator is resumed, execution continues from the point where yield was called.
"""
def count_up_to(n):
    count = 1
    while count <= n:
        yield count  # Pause the function and return the value of `count`
        count += 1

# Create a generator object
counter = count_up_to(5)

# Iterate over the generator
for num in counter:
    print(num)
