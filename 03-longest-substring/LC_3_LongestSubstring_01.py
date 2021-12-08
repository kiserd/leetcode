# Author: Donald Logan Kiser
# Date: 08/16/2020
# Description: LeetCode problem 3 Longest substring without repeating characters
#              new attempt at more efficient solution.

# Notes: work through array while logging new characters to a dictionary (paired)
# with their index. When a previously occuring char is encountered, test whether
# the distance between it and the previous occurence is a new largest substring.
# Finally, adjust the new start of your substring testing.


def lengthOfLongestSubstring(s: str) -> int:
    # define some convenient variables to help process the string
    str_size = 0
    str_begin = 0
    chars = {}

    # loop through chars in string
    for index in range(len(s)):
        # handle case where char is new
        if s[index] not in chars:
            if str_size < index - str_begin + 1:
                str_size = index - str_begin + 1
        
        # handle case where char is NOT new, but occured before str_begin
        if s[index] in chars and chars[s[index]] < str_begin:
            if str_size < index - str_begin + 1:
                str_size = index - str_begin + 1
        
        # handle case where char is NOT new
        elif s[index] in chars and chars[s[index]] >= str_begin:
            str_begin = chars[s[index]] + 1

        # update the dict value for our used char to the current occurence
        chars[s[index]] = index
    
    return str_size