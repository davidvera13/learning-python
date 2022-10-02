shopping_list = [
    "milk",
    "pasta",
    "eggs",
    "spam",
    "bread",
    "rice"
]

another_shopping_list = shopping_list
print(shopping_list)
print(another_shopping_list)
print(id(shopping_list))
print(id(another_shopping_list))

print()
shopping_list += ["cookies"]
print(shopping_list)
print(another_shopping_list)
print(id(shopping_list))
print(id(another_shopping_list))

a = b = c = d = e = f = another_shopping_list
# a = another_shopping_list
# b = another_shopping_list
# c = another_shopping_list
# d = another_shopping_list
# e = another_shopping_list
# f = another_shopping_list
print()
print(a)
print("Adding cream on b")
b.append("Cream")
print(c)
print(d)


