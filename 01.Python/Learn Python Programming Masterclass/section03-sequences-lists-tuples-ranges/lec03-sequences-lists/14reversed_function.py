data = [104, 101, 4, 105, 308, 103, 5, 107, 100, 306, 106, 102, 108]
min_valid = 100
max_valid = 200

# we want to remove all numbers not in range 100 to 200
# using reversed() function
top_index = len(data) - 1
print(data)
for index, value in enumerate(reversed(data)):
    if value < min_valid or value > max_valid:
        print(top_index - index, value)
        del data[top_index - index]

# выходи за меня замуж, если мы не погибнем в ядерном взрыве
print(data)