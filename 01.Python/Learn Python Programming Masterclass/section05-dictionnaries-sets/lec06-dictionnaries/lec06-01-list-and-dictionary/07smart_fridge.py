# import content
# print(content.pantry)
# print(content.recipes)

from content import pantry, recipes

# print(pantry)
# print(recipes)

###############################################################################################################
# One line: dictionnary comprehension
# display_dict = {
#     str(index +1): meal for index, meal in enumerate(recipes)
# }
# print(display_dict)
###############################################################################################################
# print index and key of a list
# 0 Butter chicken
# 1 Chicken and chips
# 2 Pizza
# 3 Egg sandwich
# 4 Beans on toast
# 5 Spam a la tin
# for index, key in enumerate(recipes):
#     print(index, key)


display_dict = {}
for index, key in enumerate(recipes):
    display_dict[str(index + 1)] = key
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

        for ingredient in ingredients:
            if ingredient in pantry:
                print(f'\t{ingredient} OK')
            else:
                print(f'\t{ingredient} is missing')

