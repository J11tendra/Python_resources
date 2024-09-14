# Variables defined outside the functions has a global scope and vice versa

# Global variable
name = "Jeet"


def print_name(name):
    name = "Kinsin"  # uses local variable
    print(name)


print_name(name)


# local functions
def print_another_name():
    global name
    name = "Maria"

    def new_function(name): # local function
        name = "Joma"
        print(name)

    new_function(name)


print_another_name()
