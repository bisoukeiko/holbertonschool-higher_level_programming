#!/usr/bin/python3

def weight_average(my_list=[]):

    if not my_list:
        return 0

    total = 0
    sum = 0

    for index in range(len(my_list)):
        total += my_list[index][0] * my_list[index][1]
        sum += my_list[index][1]

    return total / sum
