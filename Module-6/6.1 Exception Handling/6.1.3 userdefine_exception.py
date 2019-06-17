# A python program to create user-defined exception   
# class MyError is derived from super class Exception 
class MyError(Exception): 
  
    def __init__(self, value): 
        self.value = value 
  
  
    def __str__(self): 
        return(repr(self.value)) 
  
try: 
    raise(MyError(3*2)) 
  
except MyError as error: 
    print('A New Exception occured: ',error.value) 