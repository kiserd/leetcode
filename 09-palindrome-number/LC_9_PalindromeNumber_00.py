# Author: Donald Logan Kiser
# Date: 08/26/2020
# Description: LeetCode problem 9 Palindrome Number

def isPalindrome(x: int) -> bool:
    # convert to string
    x_str = str(x)

    # iterate through chars comparing for palindrome property
    i_beg = 0
    i_end = len(x_str) - 1
    while i_beg < i_end:
        if x_str[i_beg] != x_str[i_end]:
            return False
        i_beg += 1
        i_end -= 1
    
    # full string checked, okay to return True
    return True
    
