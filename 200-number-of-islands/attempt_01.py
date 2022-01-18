class Solution:
    def numIslands(self, grid) -> int:
        # build set of nodes to visit
        to_visit = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    to_visit.add((i, j))
        # use bfs in counting connected components
        count = 0
        visited = set()
        while to_visit:
            # print('to_visit.pop(): ', to_visit.pop())
            curr = [to_visit.pop()]
            while curr:
                i, j = curr.pop()
                visited.add((i, j))
                for row, col in [(i - 1, j), (i, j - 1), (i + 1, j), (i, j + 1)]:
                    if (row, col) in to_visit:
                        to_visit.remove((row, col))
                        curr.append((row, col))
            count += 1
        return count


        


