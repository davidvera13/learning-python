for index, char in enumerate("abcdefgh"):
    print(index, char)

print("*****************")
# output tuples
for tup in enumerate("abcdefgh"):
    # print(tup)
    index, char = tup
    print(index, char)

print("*****************")
index, char = (0, 'a')
print(index)
print(char)
