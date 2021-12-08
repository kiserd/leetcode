# Author: Donald Logan Kiser
# Date: 06/03/2021
# Description: Attempt #1 at LeetCode problem 14
#              Longest Common Prefix


def longestCommonPrefix(strs):
    # setup helper variables
    prefix = ""
    index = 0
    while True:
        char = None
        for str in strs:
            # handle case of first string in strs list
            if char is None:
                try:
                    char = str[index]
                except:
                    return prefix
            # handle case of subsequent string in strs list
            else:
                try:
                    if char != str[index]:
                        return prefix
                except:
                    return prefix
            
        # add char to prefix and increment index
        prefix += char
        index += 1
