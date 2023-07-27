from contentWithQty import pantry, recipes

display_dict = {}
for index, key in enumerate(recipes):
    display_dict[str(index + 1)] = key

# adding a shopping list to take missing ingredients
shopping_list = []


def add_shopping_item(data: list, item: str, amount: int) -> None:
    """Add a tuple containing item and amount to the data list"""
    data.append((item, amount))


# same with dictionary
shopping_list_dict = {}


def add_shopping_item_dict(data: dict, item: str, amount: int) -> None:
    """Add a tuple containing item and amount to the data dict"""
    # we can make this shorter with default
    # if item in data:
    #     data[item] += amount
    # else:
    #     data[item] = amount
    data[item] = data.setdefault(item, 0) + amount



while True:
    # display a menu of the recipes we know how to cook
    print("Please choose a recipe")
    print("*****************************************************************")
    # display list of items
    for key, value in display_dict.items():
        print(f"{key}: {value}")

    choice = input('> ')

    # we break app if we type 0
    if choice == "0":
        break
    elif choice in display_dict:
        selected_item = display_dict[choice]
        print(f"You selected { selected_item }")
        print("Checking ingredients... ")
        ingredients = recipes[selected_item]
        print(ingredients)
        # dictionary
        for ingredient, required_quantity in ingredients.items():
            # 0 is here the default value
            available_quantity_in_pantry = pantry.get(ingredient, 0)
            if required_quantity <= available_quantity_in_pantry:
                print(f'\t{ingredient} OK')
            else:
                quantity_to_buy = required_quantity - available_quantity_in_pantry
                print(f'\tYou need to buy {quantity_to_buy} of {ingredient}')
                add_shopping_item(shopping_list, ingredient, quantity_to_buy)
                add_shopping_item_dict(shopping_list_dict, ingredient, quantity_to_buy)

# printing shopping list
# using tuples we have bread twice and it doesn't sum values required 80 + 40
# ('bread', 80)
# ('butter', 10)
# ('potatoes', 3)
# ('salt', 1)
# ('malt vinegar', 5)
# ('beans', 1)
# ('bread', 40)
# for items in shopping_list:
#     print(items)

# We could sort values ...
for items in sorted(shopping_list):
    print(items)

print("*************************************")

# if we use dict
for items in shopping_list_dict.items():
    print(items)

