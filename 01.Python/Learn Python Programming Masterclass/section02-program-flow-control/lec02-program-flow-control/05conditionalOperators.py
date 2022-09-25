answer = 5

print("Please guess number between 1 and 10: ")
guess = int(input())

if guess != answer:
    if guess < answer:
        print("Please guess higher")
    else:  # guess must be greater than the answer
        print("Please guess lower")
    guess = int(input())
    if guess == answer:
        print("Well done ! you got it")
    else:
        print("Sorry, you din't guess")
else:
    print("You got it first time")
        


# if guess < answer:
#     print("Please guess higher")
#     guess = int(input())
#     if guess == answer:
#         print("Well done ! you got it")
#     else:
#         print("Sorry, you din't guess")
# elif guess > answer:
#     print("Please guess lower")
#     guess = int(input())
#     if guess == answer:
#         print("Well done ! you got it")
#     else:
#         print("Sorry, you din't guess")
# else:
#     print("You got it first time")