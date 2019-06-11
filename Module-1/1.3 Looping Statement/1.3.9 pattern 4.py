"""
A
AB
ABC
ABCD
ABCDE

"""

for i in range(1, 6):
   for j in range(65, 65+i):
       a = chr(j)
       print(a,end="")
   print()
