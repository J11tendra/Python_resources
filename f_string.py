# String

player = "Jeet"
health = 10

# method 1
print(player + " has " + str(health) + " health left.")

# method 2
print("\n%s has %s health left." % ("Jeet", 12))

# method 3
print("{} has {} health left.".format("Jeet", 19))

# method 4
print("{1} has {0} health left.".format(24, "Jeet"))

# method 5
print("{player} has {health} health left.".format(player="Jeet", health=17))

game = {
    "player": "Jeet",
    "health": 12,
}

# method 6
print("{player} has {health} health left.".format(**game))

# method 7
print(f"{player} has {health} health left.")
