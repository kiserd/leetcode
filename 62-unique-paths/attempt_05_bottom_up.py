class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # handle edge case
        if n == 1:
            return 1
        last_row = [0] * n
        prev = 1
        for _ in range(1, m + 1):
            prev = 1
            for col in range(1, n):
                prev = last_row[col] = prev + last_row[col]
        return last_row[-1]
