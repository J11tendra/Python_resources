# Dictionaries is collection of key-value pairs

# Create Dict using curly braces '{}'
user = {
    "name": "Carl Eckman",
    "gender": "Male",
    "isAdmin": False,
    "time_active_mins": 150,
}

print(user)

# Create Dict using dict() constructor
user_1 = dict(user_name="Pokefar", squad="pelot", highest_score= 1203)

print(user)
print(user_1)


# Access the items from the dict
print(user["time_active_mins"])
print(user.get("gender"))

# list all the keys
print(user_1.keys())

# list all the values
print(user_1.values())

# list all the key-value pairs as tuples
print(user.items())


# Modify the dict
user["isAdmin"] = True
user.update({"game_played": 123, "isAdmin": False})

print(user)


# Remove items
print(user.pop("gender")) # value
print(user)

print(user.popitem()) # tuple
print(user)


# Delete and clear items
del user["time_active_mins"]
user.clear() # empty dict

print(user)

del user # permanent delete


# Copy a dict
user_2 = user_1 # create a reference-it's a bad copy

user_2 = user_1.copy() # create a copy-it's a good copy
user_2["new_name"] = "Jackson"

print(user_2)
print(user_1)


# Nesting dict
student_1 = {
    'name': "rahan",
    "grade": 4,
}

student_2 = {
    'name': "yamal",
    "grade": 7,
}

school = {
    "student1": student_1,
    "student2": student_2,
}

print(school["student1"]["grade"])
print(school["student2"]["name"])
