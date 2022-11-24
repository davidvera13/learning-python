def multiply(x, y):
    # print("Multiply called")
    result = x * y
    return result


print(multiply(4, 5))
print(multiply(10.5, 4))

print()
for val in range(1, 5):
    print(multiply(val, 2))