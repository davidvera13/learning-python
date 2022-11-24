numbers = (0, 1, 2, 3, 4, 5)
print(numbers)
# unpack the tuple
print(*numbers)


print(numbers, sep=";")
print(*numbers, sep=";")
print(0, 1, 2, 3, 4, 5, sep=";")


def test_star(*args):
    print(args)
    for arg in args:
        print(arg)


test_star(0, 1, 2, 3, 4, 5)
print("empty")
test_star()

