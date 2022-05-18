# initial attempt utilized binary search in finding the
# 'closest' element, then formed bounds around it.

# it would be much easier to find a bound directly

class Solution:
    def findClosestElements(self, arr, k: int, x: int):
        lo = 0
        hi = len(arr) - k
        while lo < hi:
            mid = (lo + hi) // 2
            left = abs(arr[mid] - x)
            right = abs(arr[mid + k] - x)
            # all we know for sure is that this left bound
            # is NOT the beginning of the range
            if left > right:
                lo = mid + 1
            # all we know for sure is that this left bound
            # MIGHT be the beginning of the range
            elif left < right:
                hi = mid
            # things get tricky when we have equality
            elif left == right:
                # all we know for sure is that the range
                # can't be any higher than this
                if arr[mid] <= x <= arr[mid + k]:
                    hi = mid
                # need to shift left in edge case where
                # we have series of equal elements
                elif x < arr[mid]:
                    hi = mid - 1
                # see above comment, similar but shift right
                elif arr[mid + k] < x:
                    lo = mid + 1
        return arr[lo:lo+k]
