#  reference to mutable objects
animals = {
    "lion": ["scary", "big", "cat?"],
    "elephant": ["big", "grey", "wrinkled"],
    "teddy": "cuddly"
}

# pointing to the same object
things = animals
animals["teddy"] = "toy"
print(things["teddy"])

# pointing to a new object, not updated
new_things = animals.copy()
animals["teddy"] = "bear"
print(animals["teddy"])
print(new_things["teddy"])


print("*****************************")
print(animals["lion"])
print(new_things["lion"])
print()
new_things["lion"].append("king")
print(animals["lion"])
print(new_things["lion"])
print()


