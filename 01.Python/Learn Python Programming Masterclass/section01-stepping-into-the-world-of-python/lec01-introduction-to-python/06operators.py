# built-in datatypes classified as:
# numeric, iterator, sequence, mapping, file, class, exception
# int, float, decimal, complex (long disappeared) => int type replaces long

a = 12
b = 3
print(a)
print(b)

print(a + b)    # 15
print(a - b)    # 9
print(a * b)    # 36
print(a / b)    # 4.0 => result is float
print(a // b)   # 4 integer division, rounded down towards minus infinity
print(a % b)    # 0 remainder / modulo

print()

# expression
for i in range(1, a // b):
    print(i)