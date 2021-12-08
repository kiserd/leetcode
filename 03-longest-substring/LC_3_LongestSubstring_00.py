# Author: Donald Logan Kiser
# Date: 08/16/2020
# Description: LeetCode problem 3 Longest substring without repeating characters


def lengthOfLongestSubstring(s: str) -> int:
    start_index = 0
    longest_string = ""
    string_size = len(longest_string)
    while start_index < len(s) - string_size:
        dup = False
        current_index = start_index
        current_arr = []
        while current_index < len(s) and not dup:
            if s[current_index] not in current_arr:
                current_arr.append(s[current_index])
                current_index += 1
            else:
                dup = True
        if len(current_arr) > string_size:
            longest_string = ""
            for i in range(len(current_arr)):
                longest_string += current_arr[i]
            string_size = len(longest_string)
        
        start_index += 1
    return string_size




