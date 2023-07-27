#  copy...
lion_list = ["scary", "big", "cat?"]
elephant_list = ["big", "grey", "wrinkled"]
teddy_list = ["cuddly", "stuffed"]

animals = {
    "lion": lion_list,
    "elephant": elephant_list,
    "teddy": teddy_list
}

# things = animals.copy()
things = {
    "lion": lion_list,
    "elephant": elephant_list,
    "teddy": teddy_list
}


print(things["teddy"])
print(animals["teddy"])
print()

# same list we ovewrite and get latest value
animals['teddy'].append("added via animals dictionary")
things['teddy'].append("added via things dictionary")

print(things["teddy"])
print(animals["teddy"])
