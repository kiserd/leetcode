class Solution:
    def minimumTotal(self, triangle) -> int:
        prev = triangle[len(triangle) - 1]
        i = len(triangle) - 2
        while i > -1:
            curr = []
            for j in range(i + 1):
                curr.append(min(prev[j], prev[j + 1]) + triangle[i][j])
            prev = curr
            i -= 1
        return prev[0]