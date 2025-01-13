import re

# Example 1: Using match() to check if the pattern is at the beginning of the string
pattern = r"Hello"
string = "Hello, world!"
result = re.match(pattern, string)

if result:
    print("Match found!")
else:
    print("No match found!")
