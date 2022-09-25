numbers = "9,223;372:036 854,775;807"
separators = numbers[1::4]
print(separators)

# we join all chars that are not in separators. If we have separator, we replace by space
values = "".join(char if char not in separators else " " for char in numbers).split()
# print(str(values))
print([int(val) for val in values])

print("-" * 60)
separators = ""
for char in numbers:
    if not char.isnumeric():
        separators = separators + char

print(separators)
values = "".join(char if char not in separators else " " for char in numbers).split()
# print(str(values))
print([int(val) for val in values])

