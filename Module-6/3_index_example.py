my_list = [1, 2, 3]
try:
    print(my_list[5])  # Accessing an index that doesn't exist
except IndexError:
    print("Error: Index is out of range.")
