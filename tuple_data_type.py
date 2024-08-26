# - Tuple are unmutable data type similar to lists

my_tuple = (12, 24, 65, 2)
print(my_tuple)
print(type(my_tuple))

# If you want to add an item to a tuple;
# You can create a list, add the item, and create a new tuple

new_tuple = list(my_tuple)
new_tuple.append("Ana")
updated_tuple = tuple(new_tuple)
print(new_tuple)
print(updated_tuple)
