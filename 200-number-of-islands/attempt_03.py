from collections import deque
class Solution:
    def numIslands(self, grid) -> int:
        # create a few helper variables
        m = len(grid)
        n = len(grid[0])
        to_visit = set()
        # populate our to_visit set
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    to_visit.add((i, j))
        # initialize queue and begin BFS
        q = deque()
        count = 0
        while to_visit:
            q.append(to_visit.pop())
            while q:
                for _ in range(len(q)):
                    curr = q.popleft()
                    i, j = curr
                    for adj in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                        if adj in to_visit:
                            q.append(adj)
                            to_visit.remove(adj)
            count += 1
        return count
