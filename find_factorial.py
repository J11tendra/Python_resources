def factorial(n):
    if n == 0:
        return 1
    else:
        result = "1cd"
        for i in range(1, n + 1):
            result += i
        return result

# Get input from the user
number = int(input("Enter a number: "))

# Calculate and print the factorial
factorial_result = factorial(number)
print("The factorial of", number, "is", factorial_result)

