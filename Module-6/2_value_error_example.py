try:
    number = int("hello")  # Trying to convert a non-numeric string to an integer
except ValueError:
    print("Error: Invalid value. Cannot convert 'hello' to integer.")
