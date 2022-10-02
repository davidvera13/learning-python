current_choice = "_"
# creating an empty list
computer_parts = []
available_parts = ["computer",  "monitor", "keyboard", "mouse", "mouse mat", "HDMI Cable", "DVD Drive"]

# list comprehension: we build an array with n items.
# the items are in range between 1 and length of available parts array
valid_choices = [str(i) for i in range(1, len(available_parts) + 1)]
# long version of the one line
# valid_choices = []
# for i in range (1, len(available_parts)):
#     valid_choices.append(i)
#
# print(valid_choices)

while current_choice != "0":
    # if current_choice in "1234567":
    if current_choice in valid_choices:

        index = int(current_choice) - 1
        chosen_part = available_parts[index]
        if chosen_part in computer_parts:
            # already in, so we remove it
            print("Removing {}".format(current_choice))
            computer_parts.remove(chosen_part)
        else:
            print("Adding {}".format(current_choice))
            computer_parts.append(chosen_part)

        print("Your list contains : {}".format(computer_parts))

        # for index, part in enumerate(available_parts):
        #     if current_choice == str(index + 1):
        #         computer_parts.append(part)

        # for part in computer_parts:
        # if current_choice == '1':
        #     computer_parts.append("computer")
        # elif current_choice == '2':
        #     computer_parts.append("monitor")
        # elif current_choice == '3':
        #     computer_parts.append("keyboard")
        # elif current_choice == '4':
        #     computer_parts.append("mouse")
        # elif current_choice == '5':
        #     computer_parts.append("mouse_mat")
        # elif current_choice == '6':
        #     computer_parts.append("hdmi_cable")
    else:
        print("Please add options from the list below:")
        for index, part in enumerate(available_parts):
            # print("{0}: {1}".format(available_parts.index(part) + 1, part))
            print("{0}: {1}".format(index + 1, part))
        print("0: to finish")

    current_choice = input()

print(computer_parts)



