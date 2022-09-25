numbers = input("Enter numbers using any separators")
separators = ""

for char in numbers:
    if not char.isnumeric():
        separators = separators + char

print(separators)
values = "".join(char if char not in separators else " " for char in numbers).split()
# print(str(values))
print([int(val) for val in values])
print(sum(int(val) for val in values))
