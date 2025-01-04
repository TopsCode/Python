
even_list = [] 
odd_list = [] 

for i in range(1,6):
    num = int(input("Enter a number : "))
    if num%2==0:
        even_list.append(num)
    else:
        odd_list.append(num)

print()