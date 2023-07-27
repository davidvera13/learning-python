# using a dictionary
dictionary = {
    0: "zero",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    'iv': "four",

}

# using a list
pantry_items = ['chicken', 'spam', 'eggs', 'bread', 'lemon']

# converting a list to dictionary
pantry_items_as_dictionary = dict.fromkeys(pantry_items)
print(pantry_items_as_dictionary)
# {'chicken': None, 'spam': None, 'eggs': None, 'bread': None, 'lemon': None}

print("**********************************")

pantry_items_as_dictionary = dict.fromkeys(pantry_items, 0)
print(pantry_items_as_dictionary)
# {'chicken': 0, 'spam': 0, 'eggs': 0, 'bread': 0, 'lemon': 0}

print("**********************************")
# get keys from dictionary
keys = dictionary.keys()
print(keys)

# get values from dictionary
values = dictionary.values()
print(values)


print("**********************************")
# iterate dictionary
for item in dictionary:
    print(item)


print("**********************************")
other_dictionary = {
    7: 'lucky seven',
    10: 'ten',
    3: 'this is the new three'
}

# update and add key values in another dictionary
dictionary.update(other_dictionary)
for key, value in dictionary.items():
    print(key, value)


print("**********************************")
dictionary.update(pantry_items_as_dictionary)
for key, value in dictionary.items():
    print(key, value)



print("**********************************")
# more on values
print("four" in dictionary.values())
print("eleven" in dictionary.values())

keys = list(dictionary.keys())
values = list(dictionary.values())

print(keys)
print(values)

# not really efficient
if "four" in values:
    index = values.index("four")
    key = keys[index]
    print(f"{dictionary[key]} was found with key {key}")

# same result
for key, value in dictionary.items():
    if value == "four":
        print(f"{dictionary[key]} was found with key {key}")

