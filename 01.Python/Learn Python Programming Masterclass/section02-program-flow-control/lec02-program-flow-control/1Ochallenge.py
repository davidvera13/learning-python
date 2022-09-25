# remember that human languagees are not always very precise
# someone counts as over 18 from 1 second after midnight on their birthday
# their actual age equals to 18, but they're counted as being over 18 when
# considering things like voting or getting a credit card
name = input("Please enter your name: ")
age = int(input("How old are you? "))

if 18 <= age < 31:
    print("Welcome to club 18-30 holidays, {0}".format(name))
else:
    print("I'm sorry, our holidays are only for cool people")


