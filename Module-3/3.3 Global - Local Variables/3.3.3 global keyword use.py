# with global keyword 

"""
def myfun():
       print(name)
       name="Python Language"
       print(name)
name="Python"
myfun()
print(name)

"""

# with global keyword
def myfun():
       global name
       print("1st ",name)
       name="Python Language"
       print("2nd ",name)

name="Python"

myfun()

print("3rd ",name)
