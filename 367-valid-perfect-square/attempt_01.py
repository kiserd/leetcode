class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        # handle small cases to improve efficiency later
        if num < 5:
            if num == 1 or num == 4:
                return True
        # use binary search
        lo = 3
        hi = num // 2
        while lo <= hi:
            mid = (lo + hi) // 2
            if mid**2 == num:
                return True
            if mid**2 > num:
                hi = mid - 1
            else:
                lo = mid + 1
        return False
