class Solution:
    def mySqrt(self, x: int) -> int:
        # handle edge cases
        if x < 2:
            return x
        lo = 2
        hi = x // 2
        while lo <= hi:
            mid = (hi + lo) // 2
            if mid ** 2 == x:
                return mid
            if mid ** 2 < x:
                lo = mid + 1
            else:
                hi = mid - 1
        return hi
