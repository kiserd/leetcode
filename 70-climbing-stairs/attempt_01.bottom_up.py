class Solution:
    def climbStairs(self, n: int) -> int:
        # handle base case
        if n == 1:
            return 1
        # initialize variables to track number of ways to reach steps that
        # current step is reachable from
        two_back = 1
        one_back = 2
        # build up to nth step
        for i in range(3, n + 1):
            curr = two_back + one_back
            two_back = one_back
            one_back = curr
        return one_back


# dp[i][j] = number of ways to reach the jth step taking UP TO i - 1 length
# steps PLUS number of ways to reach the j - i step taking UP TO i length
# steps