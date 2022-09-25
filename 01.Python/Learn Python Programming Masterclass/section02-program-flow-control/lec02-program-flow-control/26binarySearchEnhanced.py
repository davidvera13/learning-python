low = 1
high = 1000

print("Please think of a number between {} and {}". format(low, high))
input('Please enter to start')


guesses = 1
while low != high:
    print("> Guessing in the range of {} to {}".format(low, high))
    guess = low + (high - low) // 2
    high_low = input("My guess is {}. Should i guess higher or lower ? "
                     "Enter h for higher, l for lower or c for correct answer"
                     .format(guess).casefold())
    if high_low == "h":
        low = guess + 1
    elif high_low == "l":
        high = guess - 1
    elif high_low == "c":
        print("I got in {} guesses! ".format(guesses))
        break
    else:
        print("Please enter h, l, c")

    guesses += 1
else:
    print("You were thinking of the number {}".format(low))
    print("I got in {} guesses! ".format(guesses))
