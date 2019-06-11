# dict as parameter
def student(**dict):

   for key,value in dict.items():
       print(key,value)

student(name="Anjali",marks=99)
