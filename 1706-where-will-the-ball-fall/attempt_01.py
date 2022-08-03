from typing import List


class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        m = len(grid)
        n = len(grid[0])
        state = [i for i in range(n)]
        for row in range(m):
            for ball in range(n):
                col = state[ball]
                if col != -1:
                    vec = grid[row][col]
                    if vec + col < 0 or vec + col > n - 1:
                        state[ball] = -1
                    else:
                        if vec == grid[row][col + vec]:
                            state[ball] += vec
                        else:
                            state[ball] = -1
        return state
