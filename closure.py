# Closure is having access to scope of parent function
# after it has returned

def coin_game(player, health):
    # health = 5

    def play_game():
        nonlocal health
        health -= 1
        if health >= 1:
            print(f'{player} has {health} health left.')
        elif health == 0:
            print(f'BooYaah!! {player} is out of health.')
    
    return play_game

jeet = coin_game("Jeet", 10)

jeet()
jeet()
jeet()
jeet()
jeet()
