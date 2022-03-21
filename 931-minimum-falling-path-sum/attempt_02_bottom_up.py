import math
class Solution:
    def minFallingPathSum(self, matrix) -> int:
        n = len(matrix)
        prev = [elt for elt in matrix[n - 1]]
        i = n - 2
        while i > -1:
            curr = []
            for j in range(n):
                cols = [max(0, j - 1), j, min(n - 1, j + 1)]
                min_val = math.inf
                for col in cols:
                    min_val = min(min_val, prev[col])
                curr.append(min_val + matrix[i][j])
            prev = curr
            i -= 1
        return min(prev)