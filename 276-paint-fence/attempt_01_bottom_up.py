# bottom-up
class Solution:
    def numWays(self, n: int, k: int) -> int:
        # handle base case
        if n == 1:
            return k
        # initialize memo array and populate base cases
        two_posts_back = k
        one_posts_back = k * k
        # iterate through number of fence posts
        for i in range(2, n, 1):
            # one way to choose same color, k ways to color last two same
            same_color = 1 * (k - 1) * two_posts_back
            # k ways to choose different color, last two posts don't matter
            different_color = (k - 1) * one_posts_back
            # shift remembered posts forward by a post
            two_posts_back = one_posts_back
            one_posts_back = same_color + different_color
        return one_posts_back

