# from start, to end value minus 1
# last value not included
for i in range(1, 20):
    print("i is now {}".format(i))

print("-" * 60)
# for 0 to 9
for i in range(10):
    print("i is now {}".format(i))

print("-" * 60)
# with step of 2
for i in range(1, 20, 2):
    print("i is now {}".format(i))

print("-" * 60)
# backwards... for 10 to 2, with step of 1
for i in range(10, 1, -1):
    print("i is now {}".format(i))


#  check if value exist
age = int(input('How old are you ?'))
if 18 <= age <= 65:
    print('Go to work')
else:
    print('Enjoy free time')

if age in range(18, 65):
    print('Go to work too')
else:
    print('Enjoy free time too')

