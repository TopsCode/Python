my_set = {1, 2, 3, 4}
my_set.remove(2)  # Removes 2 from the set
# my_set.remove(10)  # This will raise a KeyError because 10 is not in the set

my_set.discard(10)  # Does nothing as 10 is not in the set

print(my_set)  # Output: {1, 3, 4}
