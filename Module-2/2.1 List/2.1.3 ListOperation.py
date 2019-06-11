# List operations

a=[]
for x in range(10):
    a.append(x**2)
        
print(a)
print(max(a))
print(min(a))

b=[10,20,30,40,50]
a.extend(b)
print(a)
a.insert(3, 10)
print(a)
print(a.count(10))