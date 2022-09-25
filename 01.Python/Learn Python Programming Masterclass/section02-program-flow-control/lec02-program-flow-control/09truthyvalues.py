if 0:
    print("True") # code can't be executed ...
else:
    print("False")

name = input("Please enter your name")
if name:
    print("Hello {}".format(name))
else:
    print("You don't have name ?")


if name != "": # more implicit expression
    print("Hello {}".format(name))
else:
    print("You don't have name ?")
