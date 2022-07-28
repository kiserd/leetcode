class Solution:
    def climbStairs(self, n: int) -> int:
        # handle edge case
        if n < 3:
            return n
        two_back = 1
        one_back = 2
        for _ in range(3, n + 1):
            two_back, one_back = one_back, two_back + one_back
        return one_back
