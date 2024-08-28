import sys, random
from enum import Enum

# Creating a rock, paper, scissor game

class RPS(Enum):
    ROCK = 1
    PAPPER = 2
    SCISSOR = 3

playagain = True

while playagain:
    player_choice = input("\nEnter... \n1 for Rock, \n2 for Paper, \n3 for Scissors:\n\n")

    player = int(player_choice)

    if player < 1 or player > 3:
        sys.exit("You must enter 1, 2, or 3.")

    computer_choice = random.choice("123")
    computer = int(computer_choice)


    print("\nYou chose: " + str(RPS(player)).replace("RPS.", "") + ".")
    print("Computer chose: " + str(RPS(computer)).replace("RPS.", "") + ".\n")


    if player == 1 and computer == 3:
        print("🏆🏆🏆Yay, You Win!")
    elif player == 2 and computer == 1:
        print("🏆🏆🏆Yay, You Win!")
    elif player == 3 and computer == 2:
        print("🏆🏆🏆Yay, You Win!")
    elif player == computer:
        print("It's a Tie Game.")
    else:
        print("🖥🖥🖥ohho, Computer Wins!")

    playagain = input('\nPlay again? \nY for Yes or \nQ to Quit\n\n')

    if playagain.lower() == "y":
        continue
    else:
        print("\n🪅 🎊 🎉 🪅 🎊 🎉 🪅 🎊 🎉")
        print("It wouldn't be the same without you")
        playagain = False

sys.exit("\n\n........Thanks you playing.......\n\n")
