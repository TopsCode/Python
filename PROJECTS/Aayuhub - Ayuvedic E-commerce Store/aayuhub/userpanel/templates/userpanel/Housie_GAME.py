from random import * 
import os
mainlist=[]

player1=[]
player2=[]

s1=[]

status=True
os.system("cls")
while status:
    num=randint(11,99)
    if num not in mainlist:
        if len(mainlist)<12:
            mainlist.append(num)
        else:
            status=False
    else:
        status=True
    
#print("----> mainlist : ",mainlist)
print("\t\t welcome to Housyyyy ")
print("\n\n\t\t",end=" ")

for i in mainlist:
    print(i,end=" ")

player1=mainlist[6:]
player2=mainlist[:6]

print("\n====================================\n")
print("\n player 1 : ")
for i in player1:
    print(i,end=" ")

print("\n Computer : ")
for i in player2:
    print(i,end=" ")

print("\n====================================\n")

#print("\n-------------> final list is : ",mainlist)

c_status=True
while c_status:
    input("Enter :")
    num=choice(mainlist)
    
    print("selected number is : ",num)
    if num in player1:
        player1.remove(num)
        mainlist.remove(num)
        print("---> player 1 win: ",player1)
    elif num in player2:
        player2.remove(num)
        mainlist.remove(num)
        print("---> Computer win: ",player2)
        
    if len(player1)==0:
        print("\n\t ************ YOU win this game **************** ")
        c_status=False
    if len(player2)==0:
        print("\n\t ************ Computer win this game **************** ")
        c_status=False

    """
    if num in player1:
        player1.remove(num)
        print("---> player 1 win: ",player1)
    else:
        player2.remove(num)
        print("---> Computer win: ",player2)
    """

