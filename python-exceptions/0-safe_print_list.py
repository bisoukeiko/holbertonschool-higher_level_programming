#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):

    nb_print = 0

    for index in range(x):

        try:
            print(my_list[index], end="")
            nb_print += 1
        except IndexError:
            pass
    print()
    return nb_print
