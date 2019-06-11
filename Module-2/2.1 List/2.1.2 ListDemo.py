# list demo 

list1=[1,2,3,4,5]
print(list1)

list2=['Apple','Mango','Banana','Orange']
print(list2)

print(list1+list2)

if 7 in list1:
    print("2 Is Avaialable In List1")
else:
    print("2 Is Not Avaialable In List1")
    
if 'Apple' not in list2:
    print("apple Is Not Avaialable In List2")
else:
    print("apple Is Avaialable In List2")
    
print("Length Of List1 Is : ",len(list1))
print("Length Of List2 Is : ",len(list2))
print("Length Of List1 And List2 Is : ",len(list1+list2))
print([1,2,3]+[4.1,5.1,6.1])
print(['Hi']*4)

for x in list1:
    print(x,end=" ")