# While loop

count = 1

while count <= 12:
    print(count)
    count += 1


# break statement
count_01 = 1

while count_01 <= 9:
    print(count_01)
    if count_01 == 4:
        break
    count_01 += 1


# continue statement
count_02 = 1

while count_02 <= 9:
    count_02 += 1
    if count_02 == 4:
        continue
    print(count_02)
else:
    print(f'count_02 is {count_02}.')
