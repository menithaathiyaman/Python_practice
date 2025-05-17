import sys
import random
import argparse
wins=0
total_games=0
def num_guess(name='PlayerOne'):
    global wins,total_games
    playerchoice=input(f"{name},guess which number I'm thinking of...1,2 or 3.\n")

    if playerchoice not in ["1","2","3"]:
        print("Enter the valid number, you will choose only 1,2 or 3")
        return num_guess()
    player=int(playerchoice)

    if player<1 or player>3:
        sys.exit("you must enter the number from 1,2 or 3")

    print(f"{name}, your choice is ",player)
    computerchoice=random.choice("123")
    computer=int(computerchoice)
    print("computer choice is ",computer)
    
    total_games+=1

    if player==computer:
        print(f"yeah! {name}, you are right")
        print("Conguratulations.......")
        wins+=1

        
    else:
        print("I was thinking the number ",computer)
        print(f"sorry {name}. Better luck next time. ")

    print(f"Games played: {total_games}, Wins: {wins}")
    win_percentage = (wins / total_games) * 100 if total_games > 0 else 0
    print(f"Win percentage: {win_percentage:.2f}%")


    playagain = input("Play again? (y to continue / q to return to Arcade): ").lower()
    if playagain == 'q':
        print("Returning to Arcade...")
        return

# def rps_game(name='PlayerOne'):
#     while True:
#         playerchoice = input(f"Please, enter your choice {name}:\n 1 for rock \n 2 for paper \n 3 for scissors \n")
#         if playerchoice not in ["1", "2", "3"]:
#             print("You must enter 1, 2, or 3.")
#             continue

#         player = int(playerchoice)
#         computerchoice = random.choice("123")
#         computer = int(computerchoice)
#         print(f"Computer choice is {computer}")

#         if player == 1 and computer == 3:
#             print("You win!!!")
#         elif player == 2 and computer == 1:
#             print("You win!!!")
#         elif player == 3 and computer == 2:
#             print("You win!!!")
#         elif player == computer:
#             print("Match draw")
#         else:
#             print("Computer wins")

#         playagain = input("Play again? (y to continue / q to return to Arcade): ").lower()
#         if playagain == 'q':
#             print("Returning to Arcade...")
#             break
#         elif playagain != 'y':
#             print("Invalid input, returning to Arcade...")
#             break