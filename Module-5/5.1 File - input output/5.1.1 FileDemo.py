# file demo

file = open("test.txt","w")
file.write("Hello\n")
file.write("Welcome to file management program")
file.close
file = open("test.txt","r")
str=file.readline()
print(str)
a=file.tell()
print(a)
str=file.read()
print(str)