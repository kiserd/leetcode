class Solution:
    def tribonacci(self, n: int) -> int:
        # handle edge case
        if n < 3:
            return 0 if n < 1 else 1
        a = b = 1
        c = 0
        for i in range(3, n + 1):
            a, b, c = a + b + c, a, b
        return a