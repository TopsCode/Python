my_dict = {"name": "Anjali", "city": "Ahmedabad"}
try:
    print(my_dict["subject"])  # Trying to access a non-existent key
except KeyError:
    print("Error: Key not found in the dictionary.")
