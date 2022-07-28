# The isBadVersion API is already defined for you.
def isBadVersion(version: int) -> bool:
    pass


class Solution:
    def firstBadVersion(self, n: int) -> int:
        lo = 0
        hi = n
        while lo < hi:
            mid = (lo + hi) // 2
            if not isBadVersion(mid):
                lo = mid + 1
            else:
                hi = mid
        return hi
