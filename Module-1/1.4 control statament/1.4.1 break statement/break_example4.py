# break example in game implementation 

lives = 3 

status = True 

while status:
    # you can add your own game code and replace with below code 
    num = int(input("ENter a number : "))
    lives -= 1
    if lives < 1:
        break