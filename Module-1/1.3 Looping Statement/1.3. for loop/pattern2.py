"""
* * * * * 
* * * * * 
* * $ * * 
* * * * * 
* * * * * 
"""
for row in range(1,6):
    for col in range(1,6):
        if row == 3 and col == 3:
            print(" $ ",end=" ")
        else:
            print(" * ",end=" ")
    print()