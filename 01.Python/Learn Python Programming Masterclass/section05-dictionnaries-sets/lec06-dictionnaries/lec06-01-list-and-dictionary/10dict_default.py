from content import pantry

# return the value of the key if exists or return 0 if not
chicken_quantity = pantry.setdefault("chicken", 0)
print(f"chicken: {chicken_quantity}")


# beans is not in the pantry dictionary
bean_quantity = pantry.setdefault("beans", 0)
print(f"beans: {bean_quantity}")


# ketchup is not added in the pantry dictionary
ketchup_quantity = pantry.get("ketchup", 0)
print(f"ketchup: {ketchup_quantity}")

# added to dictionary
z_quantity = pantry.setdefault('zucchini', 'eight')
print(f"zucchini: {z_quantity}")


print()
print(f"Now we have in pantry! ")

for key, value in sorted(pantry.items()):
    print(key, value)