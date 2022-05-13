class Solution:
    def mySqrt(self, x: int) -> int:
        lo = 0
        hi = x
        while lo < hi:
            mid = (hi + lo + 1) // 2
            if mid ** 2 == x:
                return mid
            if mid ** 2 < x:
                lo = mid
            else:
                hi = mid - 1
        return lo
