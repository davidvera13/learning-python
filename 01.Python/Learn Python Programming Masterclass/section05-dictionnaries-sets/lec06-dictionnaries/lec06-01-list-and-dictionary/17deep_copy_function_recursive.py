from contentWithQty import recipes
import copy

def my_deepcopy(d: dict) -> dict:
    """Copy a dictionary, creating copies of the `list` or `dict` values.

    The function will crash with an AttributeError if the values aren't
    lists or dictionaries.

    :param d: The dictionary to copy.
    :return: A copy of `d`, with the values being copies of the original values.
    """

    # step 1: creating a new dictionary
    new_dict = {}
    # iterate the current dictionary and copy onto the new dictionary
    for key, value in d.items():
        new_value = value.copy()
        new_dict[key] = new_value

    return new_dict


original = {
    "Luke": ["Skywalker", ["Jedi", "tatooine"]],
    "Yoda": ["Master", ["Jedi", "Dagobah"]],
    "chewbacca": ["Unknown", ["smuggler", "Kashyyyk"]]
}

copy_1 = copy.deepcopy(original)
copy_2 = my_deepcopy(original)

# Not added to copies: edepcop use recursion to copy elements
original["Luke"].append("lightsaber")
original["chewbacca"].append("holochess")
# added to copy_2
original["chewbacca"][1].append("mechanic")
original["chewbacca"][1].append("pilot")


print(original)
print(copy_1)
print(copy_2)