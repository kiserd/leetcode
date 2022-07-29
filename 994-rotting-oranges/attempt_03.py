from collections import deque
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # define a couple convenient helper vars
        m = len(grid)
        n = len(grid[0])
        to_visit = set()
        q = deque()
        for row in range(m):
            for col in range(n):
                if grid[row][col] == 1:
                    to_visit.add((row, col))
                elif grid[row][col] == 2:
                    q.appendleft((row, col))
        # handle case of no fresh oranges
        if not to_visit:
            return 0
        # process using BFS via queue
        res = -1
        while q:
            for _ in range(len(q)):
                r, c = q.pop()
                for adj in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
                    if adj in to_visit:
                        to_visit.remove(adj)
                        q.appendleft(adj)
            res += 1
        if to_visit:
            return - 1
        return res
