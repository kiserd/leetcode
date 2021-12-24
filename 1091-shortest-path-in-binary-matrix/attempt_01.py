# trick to track distance in grid stolen from LeetCode solution
# original solution passed, but had terrible scores
class Solution:
    def shortestPathBinaryMatrix(self, grid) -> int:
        # handle edge case of 1x1 matrix
        if len(grid) == 1 and len(grid[0]) == 1:
            return 1
        # handle edge case of bottom-right cell containing 1
        if grid[len(grid) - 1][len(grid[0]) - 1] == 1:
            return -1
        # handle edge case of top-left cell containing 1
        if grid[0][0] == 1:
            return -1
        # initialize variables to help with processing
        grid[0][0] = 1
        m = len(grid)
        n = len(grid[0])
        end = [len(grid) - 1, len(grid[0]) - 1]
        queue = [[0, 0]]
        visited = [[False for i in range(n)] for i in range(m)]
        # process using bfs
        while len(queue) != 0:
            i, j = queue.pop(0)
            d = grid[i][j]
            # handle case of adjacency already explored
            if not visited[i][j]:
                visited[i][j] = True
                # handle case of exploring adjacencies
                adjs = self.get_adjacencies([i, j], m, n, visited, grid)
                # handle case of hit in adjacencies
                if end in adjs:
                    return d + 1
                # add adjacencies to queue
                for adj in adjs:
                    queue.append(adj)
                    grid[adj[0]][adj[1]] = d + 1
        # all paths explored without hit
        return -1

    
    def get_adjacencies(self, e, m, n, visited, grid):
        arr = []
        for i in range(-1, 2, 1):
            for j in range(-1, 2, 1):
                adj = [e[0] + i, e[1] + j]
                if adj[0] >= 0 and adj[0] < m and adj[1] >= 0 and \
                adj[1] < n and not visited[adj[0]][adj[1]] and grid[adj[0]][adj[1]] == 0:
                    arr.append(adj)
        return arr
