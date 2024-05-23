#!/usr/bin/python3
def no_c(my_string):
    my_list = list(my_string)
    i = 0
    while i < len(my_list):
        if my_list[i] == 'c' or my_list[i] == 'C':
            my_list.remove(my_list[i])
        else:
            i += 1
    return ''.join(my_list)
