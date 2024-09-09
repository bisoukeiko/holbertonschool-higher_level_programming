#!/usr/bin/python3

def max_integer(my_list=[]):

    if len(my_list) == 0:
        max_list = None
    else:
        max_list = 0
        for num in my_list:
            if max_list < num:
                max_list = num

    return max_list
