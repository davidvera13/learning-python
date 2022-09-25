# check value in range
age = int(input("How old are you ?"))

# Using AND
if age >= 18 and age < 65:
    print('Have a nice day at work')

if 18 <= age < 65:
    print('Have a nice day at work')
else:
    print("Enjoy your free time ...")

print("-" * 60)

# Using OR
if age < 18 or age > 56:
    print("Enjoy your free time ...")
else:
    print('Have a nice day at work')

