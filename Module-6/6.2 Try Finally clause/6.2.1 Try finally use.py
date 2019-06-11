# try finally use

try:
   print(a)
except NameError:
   print("variable a is not defined")
except:
   print("something else ")
else:
   print("Hello user")
finally:
   print("Finally block")
