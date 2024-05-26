#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    roman_letters = {
        'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1
    }

    num = 0
    last = 0

    for letter in roman_string:
        value = roman_letters.get(letter, 0)
        if value > last:
            num += value - 2 * last if last else value
        else:
            num += value
        last = value

    return num
