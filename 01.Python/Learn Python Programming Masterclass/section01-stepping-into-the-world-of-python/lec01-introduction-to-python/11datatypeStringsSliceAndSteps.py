parrot = "Norwegian Blue"
print(parrot)

# start, stop, step
print(parrot[0: 6: 2])  # Nre
print(parrot[0: 6: 3])  # Nw

numbers = "9,223,372,036,854,775,807"
print(numbers[1::4])

numbers = "9,223;372:036 854,775;807"
print(numbers[1::4])
separators = numbers[1::4]
print(separators)

values = "".join(char if char not in separators else ' ' for char in numbers).split()
print([int(value) for value in values])
