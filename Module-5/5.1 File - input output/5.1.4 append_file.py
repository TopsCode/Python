# Open the file in append mode ('a')
with open("example.txt", "a") as file:
    # Write a string to the end of the file
    file.write("This is a new line added at the end.\n")

# File is automatically closed when using the 'with' statement
