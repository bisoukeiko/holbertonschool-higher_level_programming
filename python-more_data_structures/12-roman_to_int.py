#!/usr/bin/python3

def roman_to_int(roman_string):

    roman_number = 0

    if type(roman_string) is not str or roman_string is None:
        return roman_number

    roman_dict = {"I": 1,
                  "V": 5,
                  "X": 10,
                  "L": 50,
                  "C": 100,
                  "D": 500,
                  "M": 1000}

    for idx in range(len(roman_string)):
        if idx == len(roman_string) - 1:
            roman_number += roman_dict[roman_string[idx]]

        elif roman_dict[roman_string[idx]] < roman_dict[roman_string[idx + 1]]:
            roman_number -= roman_dict[roman_string[idx]]

        else:
            roman_number += roman_dict[roman_string[idx]]

    return roman_number
