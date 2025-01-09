# This is our decorator function
def my_decorator(func):
    # This is the wrapper function that adds behavior
    def wrapper():
        print("Before calling the function")
        func()  # Call the original function
        print("After calling the function")
    
    return wrapper  # Return the wrapper function

# This is the function we want to decorate

"""
def say_hello():
    print("Hello, World!")

# Applying the decorator to the function
myfun = my_decorator(say_hello)

# Calling the decorated function
myfun()
"""
@my_decorator
def say_hello():
    print("Hello, World!")

say_hello()
