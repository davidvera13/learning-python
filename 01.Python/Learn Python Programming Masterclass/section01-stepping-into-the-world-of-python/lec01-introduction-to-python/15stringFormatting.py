# for loop
for i in range(1, 13):
    # first number refers to format value, second number refers to
    # test reserved place
    print("No. {0} squared is {1} and cubed is {2}".format(i, i ** 2, i ** 3))

print("**********************")

for i in range(1, 13):
    # first number refers to format value, second number refers to
    # test reserved place
    print("No. {0:2} squared is {1:3} and cubed is {2:4}".format(i, i ** 2, i ** 3))


print("**********************")

for i in range(1, 13):
    # < indicates the text alignment
    print("No. {0:2} squared is {1:<3} and cubed is {2:<4}".format(i, i ** 2, i ** 3))


print("**********************")

for i in range(1, 13):
    # ^ indicates the text alignment centered
    print("No. {0:2} squared is {1:^3} and cubed is {2:^4}".format(i, i ** 2, i ** 3))

print("**********************")
print("Pi is approximativelly {0:12}".format(22 / 7))
print("Pi is approximativelly {0:12f}".format(22 / 7))
print("Pi is approximativelly {0:12.50f}".format(22 / 7))
print("Pi is approximativelly {0:52.50f}".format(22 / 7))
print("Pi is approximativelly {0:62.50f}".format(22 / 7))
print("Pi is approximativelly {0:72.50f}".format(22 / 7))
