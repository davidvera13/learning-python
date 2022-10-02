even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

print(min(even))
print(min(odd))
print(max(even))
print(max(odd))

print()
print(len(even))
print(len(odd))

print()
print("mississipi".count("s"))
print("mississipi".count("iss"))

# we combine 2 lists 2, 4, 6, 8, 1, 3, 5, 7, 9
even.extend(odd)
print(even)

even.sort()
print(even)

even.sort(reverse=True)
print(even)
