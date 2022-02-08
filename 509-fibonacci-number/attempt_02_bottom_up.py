class Solution:
    def fib(self, n: int) -> int:
        # handle edge case
        if n < 2: return n
        # define recursive function
        two_back = 0
        one_back = 1
        for i in range(2, n + 1):
            one_back, two_back = one_back + two_back, one_back
        return one_back