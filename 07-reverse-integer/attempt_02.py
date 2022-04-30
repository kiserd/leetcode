class Solution:
    def reverse(self, x: int) -> int:
        # handling some housekeeping ****change this comment pls
        max_num = (2**31) - 1
        min_num = -(2**31)
        # determine whether number is negative
        neg = False
        if x < 0:
            neg = True
        # handle case of overflow when converting neg to pos
        overflow_neg = False
        if x == -(2**31):
            overflow_neg = False
        # convert from negative to positive, if applicable
        if neg:
            if overflow_neg:
                x = x // -10
            else:
                x *= -1
        # begin processing input
        res = 0
        while x != 0:
            # branch dedicated to edge case
            if overflow_neg:
                res += -(-(2**31) % -10)
                overflow_neg = False
            else:
                if res > max_num / 10:
                    return 0
                res *= 10
                rem = x % 10
                if res > max_num - rem:
                    return 0
                res += rem
                x = x // 10
        if neg:
            res *= -1
        return res
