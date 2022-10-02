# creating empty list
empty_list = []
# creating list with values
even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

#  creating list by concatenation
numbers = odd + even
print(numbers)

# using a function
sorted_numbers = sorted(numbers)
print(numbers)
print(sorted_numbers)

digits = sorted("432985617")
print(digits)

another_digit = list("432985617")
print(another_digit)

list_numbers = list(numbers)
print(list_numbers)

print(numbers is list_numbers)
print(numbers == list_numbers)

# using slice
another_list_numbers = numbers[:]
print(numbers is another_list_numbers)
print(numbers == another_list_numbers)

# copy list
last_list_numbers = numbers.copy()
print(numbers is last_list_numbers)
print(numbers == last_list_numbers)
