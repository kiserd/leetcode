# Author: Donald Logan Kiser
# Date: 08/26/2020
# Description: LeetCode problem 9 Palindromic Number attempt without
#              conversion to string first

def isPalindrome(x: int) -> bool:
    # handle case where x is negative
    if x < 0:
        return False

    # handle case where last digit is zero
    if x != 0 and x % 10 == 0:
        return False
    
    # iterate through x while separating halves
    half_1 = x
    half_2 = 0
    while half_2 < half_1:
        half_2 *= 10
        half_2 += half_1 % 10
        half_1 -= half_1 % 10
        half_1 /= 10

    # test for equality between half_1 and half_2
    if int(half_1) == int(half_2):
        return True

    # handle case where half_2 contains extra odd digit
    half_2 -= half_2 % 10
    half_2 /= 10
    if int(half_1) == int(half_2):
        return True

    # palindromic property tests failed, so return False
    return False