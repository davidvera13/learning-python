# creating a shopping list
shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]
for item in shopping_list:
    print("buy " + item)


print("-" * 60)
for item in shopping_list:
    if item != "spam":
        print("buy " + item)


print("-" * 60)
# Same result as previous
for item in shopping_list:
    if item == "spam":
        continue        # we'll reach next item in loop ...
    print("buy " + item)

print("-" * 60)
# Same result as previous
for item in shopping_list:
    if item == "spam":
        break           # will stop once value is met
    print("buy " + item)
