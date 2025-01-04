# find factorial value : 

"""
5 : 5 * 4 * 3 * 2 * 1 = 120 
"""
f = 1

num = int(input("Enter number which factorial value you want to find : "))
for i in range(1,num+1):
    f*=i

print(f"factorial value of {num} is {f}")