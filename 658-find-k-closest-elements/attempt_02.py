# attempt using template from exploration

class Solution:
    def findClosestElements(self, arr, k: int, x: int):
        lo = 0
        hi = len(arr) - k
        while lo < hi:
            mid = (lo + hi + 1) // 2
            # if we hit beginning of arr, we can safely
            # return that slice
            if mid == 0:
                return arr[:k]
            # check elements to left of current search
            left = abs(x - arr[mid - 1])
            right = abs(x - arr[mid + k - 1])
            if left < right:
                hi = mid - 1
            elif left > right:
                lo = mid
            else:
                if x >= arr[mid + k - 1]:
                    lo = mid + 1
                else:
                    hi = mid - 1
        return arr[lo:lo+k]
