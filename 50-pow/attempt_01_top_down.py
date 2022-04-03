class Solution:
    def myPow(self, x: float, n: int) -> float:
        # define recursive function
        def helper(base, exp):
            # handle base case(s)
            if exp == 0:
                return 1
            if exp == 1:
                return base
            # handle recursive case
            return base**(exp % 2) * helper(base**2, exp // 2)
        # house-keeping to prepare arguments
        if n < 0:
            n = abs(n)
            x = 1 / x
        return helper(x, n)
