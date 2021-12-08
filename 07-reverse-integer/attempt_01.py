# Author: Donald Logan Kiser
# Date: 08/26/2020
# Description: LeetCode problem 7 Reverse Integer

def reverse(x: int) -> int:
    # create variable to indicate sign and make code more readable
    neg = False
    if x < 0:
        neg = True

    # loop through digits and reverse order
    return_int = 0
    working_x = abs(x)
    while working_x != 0:
        return_int *= 10

        # test for negative overflow
        if return_int > 2147483648:
            return 0
        
        return_int += working_x % 10
        working_x -= working_x % 10
        working_x /= 10

    # test for positive overflow
    if not neg and return_int > 2147483647:
        return 0

    # negate number if necessary
    if neg:
        return_int *= -1

    return int(return_int)



    