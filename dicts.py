
# dictionaries are made up of keys and values and use {key1:val1}

dict1 = {"Bicep":"Arm Curl","Chest":"Incline Press", "Legs":"Squat", "reps":12}

# to get value of the key just print the variable with the key inside brackets

print(dict1["Bicep"])

# to get the length of the keys, just use len function

print(len(dict1))

# This allows you to delete an item from the dictionary

del dict1["Bicep"]

print(dict1)


# you can also get the value of the key by using .get
print(dict1.get("Legs"))

# prints a list of keys or values

print(dict1.keys())

print(dict1.values())
