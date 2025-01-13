import re

# Example 5: Using split() to split a string by a pattern
pattern = r"\s+"  # Matches one or more whitespace characters
string = "This is a sentence with spaces."
result = re.split(pattern, string)

print(result)  # Output: ['This', 'is', 'a', 'sentence', 'with', 'spaces.']
