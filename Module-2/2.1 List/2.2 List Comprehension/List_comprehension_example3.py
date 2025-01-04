# store all strings length in list 

# without list comprehension 
# l1 = ["C","C++","java","Python","Android"]

# l2 = [] 
# for name in l1:
#     l2.append(len(name))

# print(l2)


# with list comprehension 
l1 = ["C","C++","java","Python","Android"]

l2 = [len(name) for name in l1]

print(l2)
