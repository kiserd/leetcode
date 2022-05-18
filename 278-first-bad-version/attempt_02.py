# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        lo = 0
        hi = n
        while lo < hi:
            mid = (lo + hi) // 2
            check = isBadVersion(mid)
            if check:
                hi = mid
            else:
                lo = mid + 1
        return hi
