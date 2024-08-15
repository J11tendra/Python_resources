# String Methods

name = "Quira"

print(name)
print(name.lower())  # Lowercase
print(name.upper())  # Uppercase
print(name.title())  # Titlecase
print(len(name))  # get length


# Now, let's add some whitespace

name += "           "
name = "            " + name

print(name)
print(len(name))


# Strip the whitespace

print(len(name.strip())) # strip the whole str
print(len(name.rstrip())) # strip from the right
print(len(name.lstrip())) # strip from the left
