# - List are collection of values separated with a comma ( , ), enclosed in quotation mark
# - Lists can also have multiple data types
# - Indexing in python start with 0
# - If you know the index of an item, it can be accessed by name_of_list[index_of_item]
# - The last item has -1 index
# - Range of items can be accessed by [start:end] -- end is exclusive

users = ["Jack", "Oggy", "Maverik"]

mixed_list = ["Nobita", 12, "Shizuka", 97.6, True, "False"]

print(users)
print(mixed_list)
print("False" in mixed_list)
print(users.index("Oggy"))
print(mixed_list[0])
print(mixed_list[-1])
print(mixed_list[1:-1])

# Modifying the list
# - name_of_list.append("item_to_add") only takes one argument 
# - insert(index, item) takes 2 arguments

user_list = users[:] + mixed_list

print(user_list)

user_list.append("Espanol")
user_list.insert(1, "Ruso")

new_list = ["Bob", "Kia", "Mark"]

user_list.extend(new_list)
print(f'This is extend: {user_list}')

user_list += new_list
print(f'This is contatenation: {user_list}')


# Removing items from the list
popped_item = user_list.pop()
print(f'Popped_item: {popped_item}')

print(user_list)
user_list.remove("Mark")
del user_list[2:-1]

print(user_list)
user_list.clear()

# Sorting the list items

print("\n\n\n\n")
print("--- X ---" * 10)
print("\n\n\n\n")

num_list = [1, 3, 34, 4, 90, 7]

# num_list.sort()
print(sorted(num_list, reverse=True))
print(num_list)

str_list = ["Niel", "Henry", "ana", "Jacob", "talha", "Arun"]

str_list.sort(key=str.lower, reverse=True)
print(str_list)

# Creating a copy of list

original_list = list([1, 24, 2, 654])
copied_list = original_list.copy()
copied_list_01 = original_list[:]

print(type(original_list))
