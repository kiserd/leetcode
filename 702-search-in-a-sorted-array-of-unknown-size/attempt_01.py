# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader:
#    def get(self, index: int) -> int:

class Solution:
    def search(self, reader: 'ArrayReader', target: int) -> int:
        lo = 0
        hi = 10000
        while lo <= hi:
            mid = (lo + hi) // 2
            # handle case of "hit"
            if reader.get(mid) == target:
                return mid
            # handle case of out-of-bounds or guess too high
            if reader.get(mid) > 10000 or reader.get(mid) > target:
                hi = mid - 1
            # handle case of guess too low
            else:
                lo = mid + 1
        return -1
