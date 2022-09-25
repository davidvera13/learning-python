parrot = "Norvegian Blue"
letter = input("Enter a letter")

if letter in parrot:
    print("{} is in {}".format(letter, parrot))
else:
    print("{} was not found".format(letter))

print("-" *60)
activity = input("What do you want to do ?")
if "cinema" not in activity.casefold():
    print("Please i want to go to cinema")
else:
    print("OK let's go")

