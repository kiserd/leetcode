class Solution:
    def numIslands(self, grid) -> int:
        to_visit = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    to_visit.add((i, j))
        # process via stack, q would work too
        islands = 0
        while len(to_visit) != 0:
            islands += 1
            s = [to_visit.pop()]
            while len(s) != 0:
                i, j = s.pop()
                adjs = [(i + 1, j), (i - 1, j), (i, j - 1), (i, j + 1)]
                for adj in adjs:
                    if adj in to_visit:
                        to_visit.remove(adj)
                        s.append(adj)
        return islands