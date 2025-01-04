"""
filter only even numbers in list 
"""

l1 = [23,65,78,4,23]

l2 = [num for num in l1 if num%2==0]
print(l2)