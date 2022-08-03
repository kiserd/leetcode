class Solution:
    def isHappy(self, n: int) -> bool:
        # define helper function
        def sum_sqs(num):
            res = 0
            while num:
                res += ((num % 10)**2)
                num //= 10
            return res
        # use set to keep track of visited nums
        visited = set()
        while n != 1:
            if n in visited:
                return False
            visited.add(n)
            n = sum_sqs(n)
        return True
