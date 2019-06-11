#random module use

import random
from builtins import int 
number = random.randint(9,20)

while True:
    guess = int(input("Guess number :"))
    
    if guess==number:
        print("Guess number is correct")
        break
    if guess>number:
        print("Guess is greater than number")
    if guess<number:
        print("Guess is small than number")
    else:
        print("You guess the right number")
        
    