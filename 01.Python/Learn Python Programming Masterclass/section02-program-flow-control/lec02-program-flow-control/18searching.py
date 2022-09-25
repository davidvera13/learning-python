shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]

# item_to_find = "spam"
item_to_find = "Ham"
found_at_index = None

# using break
for index in range(len(shopping_list)):
    if shopping_list[index] == item_to_find:
        found_at_index = index
        break

if found_at_index is not None:
    print("item found at position {}".format(found_at_index))
else:
    print("{} not found".format(item_to_find))

print("-" * 60)

item_to_find = "spam"
# item_to_find = "Ham"
found_at_index = None

# using list
if item_to_find in shopping_list:
    found_at_index = shopping_list.index(item_to_find)

if found_at_index is not None:
    print("item found at position {}".format(found_at_index))
else:
    print("{} not found".format(item_to_find))


