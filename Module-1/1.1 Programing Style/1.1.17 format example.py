# basic formatting example 

name = "Anjali"
age = 25
greeting = "Hello, {} ! You are {} years old.".format(name, age)
print(greeting)

# Output: Hello, Anjali ! You are 25 years old 

# Positional Arguments: 
#
# You can use positional placeholders {} to specify where the arguments 
# will go. The first placeholder gets the first argument, the second placeholder gets the second argument, and so on.

greeting = "The first number is {} and the second is {}.".format(10, 20)
print(greeting)

# Output: The first number is 10 and the second is 20.

# Named Arguments: 
# 
# You can also use named placeholders and specify arguments by name instead of position.

greeting = "Hello, {name}! You are {age} years old.".format(name="Anjali", age=20)
print(greeting)
# Output: Hello, Anjali ! You are 25 years old.

# Reordering Arguments: 
# 
# You can reorder arguments by using index numbers in the placeholders

greeting = "The second value is {1} and the first value is {0}.".format(10, 20)
print(greeting)
# Output: The second value is 20 and the first value is 10.


# Formatting Numbers: 
# 
# You can format numbers to control the number of decimal places, add commas, 
# or specify other formats.

pi = 3.14159
formatted_string = "The value of pi is {:.2f}".format(pi)
print(formatted_string)

# Output: The value of pi is 3.14
