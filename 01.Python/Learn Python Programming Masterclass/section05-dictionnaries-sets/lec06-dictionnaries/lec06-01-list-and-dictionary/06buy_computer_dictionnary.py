available_parts = {"1": "computer",
                   "2": "monitor",
                   "3": "keyboard",
                   "4": "mouse",
                   "5": "hdmi cable",
                   "6": "dvd drive",
                   }


current_choice = None
# computer_parts = []  # create an empty list
computer_parts = {}


while current_choice != "0":
    if current_choice in available_parts:
        chosen_part = available_parts[current_choice]
        # if chosen_part in computer_parts: with list ...
        # with dict
        if current_choice in computer_parts:
            # it's already in, so remove it
            print(f"Removing {chosen_part}")
            # computer_parts.remove(chosen_part)
            computer_parts.pop(current_choice)
        else:
            print(f"Adding {chosen_part}")
            # computer_parts.append(chosen_part)
            computer_parts[current_choice] = chosen_part
        print(f"You have the following items in your cart: {computer_parts}")
    else:
        print("Please select an item from the list")
        for key, value in available_parts.items():
            print(f"{key}: {value}")
        print('0: to finish ....')

    current_choice = input("> ")

# while current_choice != '0':
#     if current_choice in valid_choices:
#         index = int(current_choice) - 1
#         chosen_part = available_parts[index]
#         if chosen_part in computer_parts:
#             # it's already in, so remove it
#             print("Removing {}".format(current_choice))
#             computer_parts.remove(chosen_part)
#         else:
#             print("Adding {}".format(current_choice))
#             computer_parts.append(chosen_part)
#         print("Your list now contains: {}"
#               .format(computer_parts))
#     else:
#         print("Please add options from the list below:")
#         for number, part in enumerate(available_parts):
#             print("{0}: {1}".format(number + 1, part))
#         print("0: to finish")
#
#     current_choice = input()
#
# print(computer_parts)