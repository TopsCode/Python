import re 

# Example 3: Using findall() to find all matches of the pattern
pattern = r"\d+"  # Matches one or more digits
string = "I have 12 apples, 15 bananas, and 100 grapes."
result = re.findall(pattern, string)

print(result)  # Output: ['12', '15', '100']
