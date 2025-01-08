# Open a file in write mode ('w'), this will overwrite the file if it already exists
file = open("example.txt", "w")

# Write a string to the file
file.write("This is the first line.\n")
file.write("This is the second line.\n")

# Close the file after writing
file.close()
