# prime number ::: 

"""
5     -   1         5 
6     - 1, 2..
   
    _3___
  2 | 6   (not a prime number)
    | 6
    ------
      0

      2
    -----
   2| 5     (prime number)
    | 4
     -----
      1

                    5
                
            (1)   2    3    4     (5)

                     6
            (1)  2--                 (6)
"""
num = int(input("Enter a number : "))#20  5 
flag = True 

for i in range(2,num):
    if num%i == 0:
        flag = False
        break
    else:
        flag = True

if flag:
    print("prime number")
else:
    print("not a prime number")