import copy

lion_list = ["scary", "big", "cat?"]
elephant_list = ["big", "grey", "wrinkled"]
teddy_list = ["cuddly", "stuffed"]

animals = {
    "lion": lion_list,
    "elephant": elephant_list,
    "teddy": teddy_list
}

# shallow copy
# things = animals.copy()

# deep copy
things = copy.deepcopy(animals)

print(things["teddy"])
print(animals["teddy"])
print()

# same list we ovewrite and get latest value
animals['teddy'].append("added via animals dictionary")
things['teddy'].append("added via things dictionary")

print(things["teddy"])
print(animals["teddy"])
# id and returned values are different, we point to 2 objects distincts
print(id(things["teddy"]), things["teddy"])
print(id(animals["teddy"]), animals["teddy"])

