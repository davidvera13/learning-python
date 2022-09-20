# index   01234567891011121314
parrot = "Norwegian Blue"
print(parrot)
# print(parrot[3])    # w

# mini challenge
# Add some code to the program to print we win
# Each character shoud appear on a separate line
# the program should get the character from the parrot string using indexes

print(parrot[3])    # w
print(parrot[4])    # e
print(parrot[9])    # ' '
print(parrot[3])    # w
print(parrot[6])    # i
print(parrot[8])    # n

print()
# negative indexing
print(parrot[-11])    # w
print(parrot[-1])     # e
print(parrot[-5])     # ' '
print(parrot[-11])    # w
print(parrot[-8])     # i
print(parrot[-6])     # n

print()
# trick
print(parrot[3 - 14])    # w
print(parrot[4 - 14])    # e
print(parrot[9 - 14])    # ' '
print(parrot[3 - 14])    # w
print(parrot[6 - 14])    # i
print(parrot[8 - 14])    # n
