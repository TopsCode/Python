"""
ROCK PAPER SCSSIOR

"""
import random 

game_list = ["R","P","S"] 

menu = """
                WELCOME TO ROCK PAPER SCISSOR GAME 

                    PRESS 'R' FOR ROCK
                    PRESS 'P' FOR PAPER
                    PRESS 'S' FOR SCISSOR
                
    """


status = True
while status:
    print(menu)
    computer = random.choice(game_list)
    user_choice = input("Enter your choice : ").upper() 
    print("COMPUTER CHOICE : ",computer)
    print("USER CHOICE : ",user_choice)
    print()
    if user_choice == "R" and computer == 'P' or user_choice == "P" and computer == "S" or user_choice == 'S' and computer == 'R': 
        print("COMPUTER WON THIS MATCH !")
    elif user_choice == "R" and computer == "S" or user_choice == 'P' and computer == 'R' or user_choice == 'S' and computer == 'p':
        print("USER WON THIS MATCH !!")
    else:
        print("TIE !")

    choice = input("Do you want to play again press 'y' for yes and press 'n' for no : ")
    if choice == 'n' or choice == 'no':
        status = False
    



