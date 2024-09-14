import sys, random
from enum import Enum

# Creating a rock, paper, scissor game


def rps():
    game_count = 0
    player_wins = 0
    computer_wins = 0

    def play_rps():
        nonlocal game_count
        nonlocal player_wins
        nonlocal computer_wins

        class RPS(Enum):
            ROCK = 1
            PAPPER = 2
            SCISSOR = 3

        player_choice = input(
            "\nEnter... \n1 for Rock, \n2 for Paper, \n3 for Scissors:\n\n"
        )

        if player_choice not in ["1", "2", "3"]:
            print("You must enter 1, 2, or 3.")
            return play_rps()

        player = int(player_choice)

        computer_choice = random.choice("123")
        computer = int(computer_choice)

        print("\nYou chose: " + str(RPS(player)).replace("RPS.", "") + ".")
        print("Computer chose: " + str(RPS(computer)).replace("RPS.", "") + ".\n")

        def choose_winner(player, computer):
            nonlocal player_wins
            nonlocal computer_wins

            if player == 1 and computer == 3:
                player_wins += 1
                print("🏆🏆🏆Yay, You Win!")
            elif player == 2 and computer == 1:
                player_wins += 1
                print("🏆🏆🏆Yay, You Win!")
            elif player == 3 and computer == 2:
                player_wins += 1
                print("🏆🏆🏆Yay, You Win!")
            elif player == computer:
                print("It's a Tie Game.")
            else:
                computer_wins += 1
                print("🖥🖥🖥ohho, Computer Wins!")

        choose_winner(player, computer)

        nonlocal game_count
        game_count += 1
        print(f"\nYour Game count: {game_count}")
        print(f"\nPlayer wins: {player_wins}")
        print(f"\nComputer wins: {computer_wins}")

        print("\nPlay again?")

        while True:
            playagain = input("\nY for Yes or \nQ to Quit\n\n")
            if playagain.lower() not in ["y", "q"]:
                continue
            else:
                break

        if playagain.lower() == "y":
            return play_rps()
        else:
            print("\n🪅 🎊 🎉 🪅 🎊 🎉 🪅 🎊 🎉")
            print("It wouldn't be the same without you")
            sys.exit("\n\n........Thanks you playing.......\n\n")

    return play_rps


play = rps()
play()
