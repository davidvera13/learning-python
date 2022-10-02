missing_letters = sorted(
    "The big brown fox jumped over the lazy dog",
    key=str.casefold)
print(missing_letters)

names = ["Graham", "John", "terry", "eric", "Terry", "michael"]
names.sort()
print(names)

names.sort(key=str.casefold)
print(names)
