# for loop

names = ["jeet", "sara", "olivia", "karan"]

for name in names:
    if name == "karan":
        print(f'Congrats {name}, You win!!')
        break
    else:
        print(f'{name}..skip')


# in range
for num in range(2, 21, 2):
    print(f'{num}')
