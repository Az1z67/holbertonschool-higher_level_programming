#!/usr/bin/python3
def uniq_add(my_list=[]):
    total = 0
    new_list = set()
    if len(my_list) > 0:
        for num in my_list:
            if num not in new_list:
                new_list.add(num)
                total += num
    return total
