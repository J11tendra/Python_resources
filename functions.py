# Simple Function
# function's name must in lowercase
# underscore can be used in middle


# Define the function
def print_hello():
    print("Hello") 

# Call the function
print_hello()


# Return Function
# functions need to return some value
def return_hello():
    return "Hello"

# Call the function
get_hello = return_hello()
print(get_hello)


# Parameters Function
def get_sum(num_01, num_02): # num_01 & num_02 are parameters (constant)
    return num_01 + num_02

# Call the function
sum = get_sum(10, 12) # 10 & 12 are arguments (can change)
print(sum)


# Default Function
def find_product(num_01 = 10, num_02 = 5):
    return num_01 * num_02

product = find_product(num_02=13)
print(product)


# Dynamic Args Function
def print_name(*args):
    return args, type(args)

print(print_name("Lapon"))

# Pass more args
print(print_name("Lapon", "klien", "Vashir"))


#

def some_function(**args):
    return args, type(args)

print(some_function(name="Uran", name_01= "Viran"))
