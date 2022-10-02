# sorting iterable objects
# a pangram contains all letters once at least
pangram = "The big brown fox jumps over the lazy dog"
sorted_letters = sorted(pangram)
print(pangram)
print(sorted_letters)

numbers = [2.3, 4.5, 8.7, 12.5, -3.14, 613]
sorted_numbers = sorted(numbers)
print(numbers)
print(sorted_numbers)

print()
# difference sort & sorted: sort modifiy the current list, sorted assign
# values to a new list
numbers.sort()
print(numbers)

another_sorted_numbers = numbers.sort()
print(another_sorted_numbers)           # None


missing_letters = sorted("The big brown fox jumped over the lazy dog")
print(missing_letters)

