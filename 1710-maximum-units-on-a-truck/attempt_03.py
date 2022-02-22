# intuitive O(1) sol stolen from discussion. Not mentioned in solution, but
# was easy to grasp quickly upon glancing over the discussion post
class Solution:
    def maximumUnits(self, boxTypes, truckSize: int) -> int:
        counter = [0] * 1001
        for qty, units_per in boxTypes:
            counter[units_per] += qty
        i = 1000
        res = 0
        while i and truckSize:
            if counter[i] > 0:
                num_used = min(counter[i], truckSize)
                res += (i * num_used)
                truckSize -= num_used
            i -= 1
        return res
