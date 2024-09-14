# Recursion happens when a function calls itself


def add_num(num):
    if num >= 10:
        return num + 1
    total = num + 1
    print(total)

    return add_num(total) # Call the function itself

total_sum = add_num(0)
print(add_num(0))
