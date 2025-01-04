words = ["hello", "world", "python"]

# Convert each word to uppercase using map and lambda
uppercase_words = map(lambda word: word.upper(), words)

print(list(uppercase_words))  # Output: ['HELLO', 'WORLD', 'PYTHON']
