lines = ["Line 1\n", "Line 2\n", "Line 3\n"]
file = open("filename.txt", "w")  # Open the file in write mode
file.writelines(lines)  # Write the list of lines to the file
file.close()  # Close the file after writing
