# write a program to check if it's a leap year or not.

# Conditions for leap year:
# 1. divisible by 4
# 2. if it is divisible by 100, then also should be divisible by 400

user_year = int(input("Enter any year:\t"))

if user_year % 4 == 0:
    if user_year % 100 == 0:
        if user_year % 400 == 0:
            print(f'{user_year} is a leap year.')
        else:
            print(f'{user_year} is not a leap year.')
    else:
        print(f'{user_year} is a leap year.')
else:
    print(f'{user_year} is not a leap year.')
