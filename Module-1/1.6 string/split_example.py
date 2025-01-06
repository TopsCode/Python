# split example 

s1 = "anjali patel"

print(s1)

s2 = s1.split() # by default split from space 
print(s2)

s3 = "python programing , java programing"
s4 = s3.split(",")
print(s4)

s3 = "python programing | java programing |flutter technology"
s4 = s3.split("|",1)
print(s4)