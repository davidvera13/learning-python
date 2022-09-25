# 2 issues:
# > the solution is always the same
# > we have only 2 tries and the game stops: solved with while

import random

highest = 10
answer = random.randint(1, highest)
max_tries = 4
tries = 0
# we initialise guess to enter the while loop and initial value must be
# out of answers range of values
guess = 0
# TODO: remove after testing
print(answer)
print("Please guess number between 1 and {}: ".format(highest))


while answer != guess:
    guess = int(input())
    if guess == 0:
        break
    if guess == answer:
        print("Well done ! you got it")
    else:
        tries += tries
        if guess > answer:
            print("Please guess higher")
            break
        else:
            print("Please guess lower")


# Old version
# answer = 5
#
#
# if guess == answer:
#     print("You got it first time")
# else:
#     if guess > answer:
#         print("Please guess higher")
#     else:
#         print("Please guess lower")
#     guess = int(input())
#     if guess == answer:
#         print("Well done ! you got it")
#     else:
#         print("Sorry, you din't guess")
#
