# We have 5 sequence types built in
# string, list, tuple, range, bytes and bytearray

str1 = "He's "
str2 = "probably "
str3 = "pining "
str4 = "for the "
str5 = "fjords"

print(str1 + str2 + str3 + str4 + str5)
print("He's " "probably " "pining " "for the " "fjords")

print("Hello " * 5)
print("Hello " * (5 + 4))
print("Hello " * 5 + "4")
# print("Hello " * 5 + 4)   # TypeError: can only concatenate str (not "int") to str

today = "thuesday"
print('day' in today)       # true
print('fri' in today)       # false
print('mon' in today)       # false
print('thues' in today)     # true
print('parrot' in 'fjord')  # false

