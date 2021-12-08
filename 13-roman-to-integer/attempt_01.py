# Author: Donald Logan Kiser
# Date: 08/26/2020
# Description: LeetCode problem 13 Roman To Integer attempt at efficient solution

def romanToInt(s: str) -> int:
    # establish dictionary of roman to int mappings
    map = {}
    map['I'] = 1
    map['V'] = 5
    map['X'] = 10
    map['L'] = 50
    map['C'] = 100
    map['D'] = 500
    map['M'] = 1000

    # handle case where input is more than one character
    return_int = map[s[-1]]
    for index in range(len(s) - 1):
        # handle case where subtraction is required
        if map[s[index]] < map[s[index + 1]]:
            return_int -= map[s[index]]
        # handle case where simple addition is required
        else:
            return_int += map[s[index]]

    return return_int