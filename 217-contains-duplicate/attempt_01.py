# naive first attempt - looks like the accepted/preferred O(n) solution
# could use Python's built-in set operation, but it might do extra ops
class Solution:
    def containsDuplicate(self, nums) -> bool:
        tracker = {}
        for num in nums:
            if num in tracker:
                return True
            else:
                tracker[num] = None
        return False
