#!/usr/bin/python3

"""
function that prints a text with 2 new lines
after each of these characters: ., ? and :
"""


def text_indentation(text):
    """
        Args:
            text(string): text
        Raises:
            TypeError: If the text is not a string.
    """

    if type(text) is not str:
        raise TypeError("text must be a string")

    for index in range(len(text)):

        if index != 0 and text[index - 1] in [".", "?", ":"]:
            continue
        else:
            print(text[index], end="")

        if text[index] in [".", "?", ":"]:
            print()
            print()
