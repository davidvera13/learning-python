def is_palindrome(string: str) -> bool:
    """
    Check if a string is a palindrome
    A palindrome is a string that reads the same forwards as backwards
    :param string: the string to check
    :return: true if `string` is a palindrome, false otherwiser
    """
    # backwards = string[::-1]
    # return backwards == string
    return string[::-1].casefold() == string.casefold()


def is_palindrome_sentence(sentence):
    string = ""
    for char in sentence:
        if char.isalnum():
            string += char

    # return string[::-1].casefold() == string.casefold()
    return is_palindrome(string)




# word = input("Please enter a word to check: ")
# if is_palindrome(word):
#     print("'{}' is a palindrome".format(word))
# else:
#     print("'{}' is not a palindrome".format(word))

sentence = input("Please enter a sentence to check: ")
if is_palindrome_sentence(sentence):
    print("'{}' is a palindrome".format(sentence))
else:
    print("'{}' is not a palindrome".format(sentence))

