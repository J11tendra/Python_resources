import sys, random
from enum import Enum

# Creating a rock, paper, scissor game

class RPS(Enum):
    ROCK = 1
    PAPPER = 2
    SCISSOR = 3

print("")
player_choice = input("Enter... \n1 for Rock, \n2 for Paper, \n3 for Scissors:\n\n")

player = int(player_choice)

if player < 1 or player > 3:
    sys.exit("You must enter 1, 2, or 3.")

computer_choice = random.choice("123")
computer = int(computer_choice)


print("")
print("You chose: " + str(RPS(player)).replace("RPS.", "") + ".")
print("Computer chose: " + str(RPS(computer)).replace("RPS.", "") + ".")
print("")


if player == 1 and computer == 3:
    print("Yay, You Win!")
elif player == 2 and computer == 1:
    print("Yay, You Win!")
elif player == 3 and computer == 2:
    print("Yay, You Win!")
elif player == computer:
    print("It's a Tie Game.")
else:
    print("ohho, Computer Wins!")
