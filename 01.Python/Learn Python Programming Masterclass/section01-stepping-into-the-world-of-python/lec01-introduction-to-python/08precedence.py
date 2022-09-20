a = 12
b = 3

print(a + b / 3 - 4 * 12)   # -35.0 not 12.0
# precedence will calculate -4*12 = -48, 3 / 3 = 1, 12+1-48...
print(a + (b / 3) - (4 * 12))

print(((a+b)/3 - 4)*12)

c = a + b
d = c / 3
e = d - 4
print(e * 12)

print(a / (b * a) / b)
