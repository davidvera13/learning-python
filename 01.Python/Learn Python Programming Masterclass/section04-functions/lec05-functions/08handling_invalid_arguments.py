# if value is passed, the variable is optional and a default value is eet
def banner_text(text=" ", screen_width=80):
    # screen_width = 50
    if len(text) > screen_width - 4:
        error_message = "String {0} is larger than specified width {1}"\
            .format(text, screen_width)
        raise ValueError(error_message)

    if text == "*":
        print("*" * screen_width)
    else:
        # centred_text = text.center(screen_width - 4)
        # output_string = "**{0}**".format(centred_text)
        # print(output_string)
        print("**{0}**".format(text.center(screen_width - 4)))


banner_text("*", 66)
banner_text("Always look on the bright side of life...", 66)
banner_text("If life seems jolly rotten,", 66)
banner_text("There's something you've forgotten!")
banner_text("And that's to laugh and smile and dance and sing,")
# banner_text(" ")
banner_text(screen_width=66)
banner_text("When you're feeling in the dumps,")
banner_text("Don't be silly chumps,")
banner_text("Just purse your lips and whistle - that's the thing!")
banner_text("And... always look on the bright side of life...")
banner_text("*", 80)

result = banner_text("Nothing is returned")
print(result)
