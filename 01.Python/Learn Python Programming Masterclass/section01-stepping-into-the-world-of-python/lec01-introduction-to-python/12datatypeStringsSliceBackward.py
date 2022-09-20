letters = "abcdefghijklmnopqrstuvwxyz"

backwards = letters[25:0:-1]
print(backwards)        # a missing
print(letters[25::-1])  # -1 wont work
print(letters[::-1])

# using the alphabet creat a slice that produces "qpo", "edcba", the 8
# last characters

print(letters[16:13:-1])
print(letters[4::-1])

print(letters[25:17:-1])
print(letters[:-9:-1])


# idioms:
print(letters[-4:])
print(letters[-5:])
print(letters[-6:])
print(letters[-1:])
print(letters[:1])
print(letters[0])

alt = ''
print(alt[:1])   # not throwing exception
# print(alt[0])    # throws an exception > IndexError: string index out of range





