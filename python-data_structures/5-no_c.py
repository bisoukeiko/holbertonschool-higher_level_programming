#!/usr/bin/python3

def no_c(my_string):

    index = 0
    while index < len(my_string):

        if my_string[index] == "c" or my_string[index] == "C":
            my_string = my_string[:index] + my_string[index + 1:]
            index -= 1

        index += 1

    return my_string
