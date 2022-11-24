# Some ANSI escape sequences for colours and effects
BLACK = '\u001b[30m'
RED = '\u001b[31m'
GREEN = '\u001b[32m'
YELLOW = '\u001b[33m'
BLUE = '\u001b[34m'
MAGENTA = '\u001b[35m'
CYAN = '\u001b[36m'
WHITE = '\u001b[37m'
RESET = '\u001b[0m'

BOLD = '\u001b[1m'
UNDERLINE = '\u001b[4m'
REVERSE = '\u001b[7m'

print(RED, "Text in red ?? ")
print(RED, UNDERLINE, "Text in red ?undeline ? ")
print("It is also red")


def colour_print(text: str, *effects: str) -> None:
    """
    Print text using ansi sequence to change colour, etc
    :param text: text to print
    :param effects: effect wanted
    :return:
    """
    effect = "".join(effects)
    output_str = "{0}{1}{2}".format(effect, text, RESET)
    print(output_str)


colour_print("Hello, Red", RED)
colour_print("Hello, Red and Bold", RED, BOLD)
# test that the colour was reset
print("This should be in the default terminal colour")
colour_print("Hello, Blue with underline", BLUE, UNDERLINE)
colour_print("Hello, Yellow", YELLOW, REVERSE)
colour_print("Hello, Bold and magenta", BOLD, MAGENTA)
colour_print("Hello, Underline and Cyan", UNDERLINE, CYAN)
colour_print("Hello, Reverse", REVERSE)
colour_print("Hello, Black", BLACK)