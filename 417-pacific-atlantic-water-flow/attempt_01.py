from typing import List
from collections import deque


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # create a couple convenient helper vars
        m = len(heights)
        n = len(heights[0])
        # determine which cells are reachable by the pacific ocean
        to_visit = set()
        pacs = set()
        for i in range(1, m):
            for j in range(1, n):
                to_visit.add((i, j))
        pac_starts = set([(0, i) for i in range(n)])
        for i in range(0, m, 1):
            pac_starts.add((i, 0))
        q = deque(list(pac_starts))
        while q:
            r, c = q.pop()
            pacs.add((r, c))
            for nr, nc in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
                if (nr, nc) in to_visit:
                    if heights[nr][nc] >= heights[r][c]:
                        q.appendleft((nr, nc))
                        to_visit.remove((nr, nc))
        # determine which are reachable by the atlantic ocean
        to_visit = set()
        for i in range(m - 1):
            for j in range(n - 1):
                to_visit.add((i, j))
        atl_starts = set([(m - 1, i) for i in range(n)])
        atls = set()
        for i in range(m):
            atl_starts.add((i, n - 1))
        q = deque(list(atl_starts))
        while q:
            r, c = q.pop()
            atls.add((r, c))
            for nr, nc in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
                if (nr, nc) in to_visit:
                    if heights[nr][nc] >= heights[r][c]:
                        q.appendleft((nr, nc))
                        to_visit.remove((nr, nc))
        intrsct = pacs.intersection(atls)
        res = []
        for r, c in intrsct:
            res.append([r, c])
        return res
