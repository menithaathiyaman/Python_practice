from numberguessing import num_guess
from rpswithname import rps_game
from gamyy import game
import sys

def main():
    name = input("Enter your name: ")
    while True:
        print("\n---- Welcome to Arcade ----")
        print("1. Rock, Paper and Scissor")
        print("2. Number Guessing")
        print("3. Hangman game")
        print("Exiting Program..")

        choice = input("Enter your choice (1/2/3): ")
        if choice == "1":
            rps_game(name)
        elif choice == "2":
            num_guess(name)
        elif choice == "3":
           game(name)
        elif choice=="4":
            print("Exit program")
            break
        else:
            print("Invalid input. Try again.")

        play_again = input("Do you want to go back to the arcade menu? (y/n): ").lower()
        if play_again != "y":
            print("Thank you for playing, bye!!")
            break

if __name__ == "__main__":
    main()
