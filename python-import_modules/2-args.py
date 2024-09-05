#!/usr/bin/python3

import sys

if __name__ == "__main__":

    len_argv = len(sys.argv) - 1
    argv = sys.argv

    if len_argv == 0:
        print("{} arguments.".format(len_argv))
    elif len_argv == 1:
        print("{} argument:".format(len_argv))
    else:
        print("{} arguments:".format(len_argv))

    for index in range(1, len_argv + 1):
        print("{}: {}".format(index, argv[index]))
