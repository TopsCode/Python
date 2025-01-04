words = ["anjali","priyanshi","om","ashvi","ram"]

# Filter strings with length greater than or equal to 4
long_words = filter(lambda word: len(word) >= 4, words)

# Convert to list and print the result
print(list(long_words)) 
