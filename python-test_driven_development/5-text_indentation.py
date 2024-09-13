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

    index = 0
    while index < len(text):

        if text[index] == " " and \
          (index == 0 or text[index - 1] in [".", "?", ":"]):
            index += 1
            continue

        print(text[index], end="")

        if text[index] in [".", "?", ":"]:
            print("\n")
            index += 1
            while index < len(text) and text[index] == " ":
                index += 1
            continue

        index += 1
