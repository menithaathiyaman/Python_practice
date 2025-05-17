import sys
import random
import argparse
def rps_game(name='playerOne'):
    playerchoice=input(f"please, Enter your choice {name}:\n 1 for rock \n 2 for paper \n 3 scissor \n")
    if playerchoice not in ["1","2","3"]:
        print("you must enter 1 ,2 or 3")
        return rps_game(name)
    player=int(playerchoice)
    if player<1 or player>3:
        sys.exit("you must enter the player value as 1, 2 or 3")
    computerchoice=random.choice("123")
    computer=int(computerchoice)
    print("computer choice is ",computer )
    if  player==1 and computer==3:
        print("you wins!!!")
    elif player==2 and computer==3:
        print("you wins!!!")
    elif player==3 and computer==2:
        print("you wins!!!")
    elif player==computer:
        print("match draw")
    else:
        print("computer wins")
    playagain = input("Enter y to play again or q to quit: ")
    if playagain.lower() == "q":
        print("Thank you for playing!")
        return

    
        
