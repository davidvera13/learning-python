low = 1
high = 1000

print("Please think of a number between {} and {}". format(low, high))
input('Please enter to start')


guesses = 1
while True:
    print("> Guessing in the range of {} to {}".format(low, high))
    guess = low + (high - low) // 2
    high_low = input("My guess is {}. Should i guess higher or lower ? "
                     "Enter h for higher, l for lower or c for correct answer"
                     .format(guess).casefold())
    if high_low == "h":
        # guess is higher. the low end becomes 1 greater than the guess
        # pass is placeholder and does nothing.
        # It's required when no code is in the statement
        # pass
        low = guess + 1
    elif high_low == "l":
        # guess is lower. the low end becomes 1 less than the guess
        high = guess - 1
    elif high_low == "c":
        print("I got in {} guesses! ".format(guesses))
    else:
        print("Please enter h, l, c")

    # guesses = guesses + 1
    # augmented assignment is more efficient, we do not have to create
    # a variable and assign a value
    guesses += 1
