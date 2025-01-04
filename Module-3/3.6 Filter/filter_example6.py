strings = ["hello", "", "world", "", "python", ""]

# Remove empty strings
non_empty_strings = filter(lambda x: x != "", strings)

# Convert to list and print the result
print(list(non_empty_strings))  # Output: ['hello', 'world', 'python']
