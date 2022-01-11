class Solution:
    def orangesRotting(self, grid) -> int:
        # define a couple helper variables
        m = len(grid)
        n = len(grid[0])
        # create list of rotten and fresh orange coords
        to_visit = []
        rotten = []
        for i in range(m):
            for j in range(n):
                # handle case where orange is fresh
                if grid[i][j] == 1:
                    to_visit.append([i, j])
                # handle case where orange is rotten
                if grid[i][j] == 2:
                    rotten.append([i, j])
        # keep track of time while BFSing from rotten
        time = 0
        new_oranges = True
        while new_oranges and len(to_visit) != 0:
            new_rottens = []
            new_oranges = False
            for row, col in rotten:
                for node in [[row - 1, col], [row + 1, col], [row, col - 1], [row, col + 1]]:
                    if node in to_visit:
                        new_rottens.append(node)
                        to_visit.remove(node)
            time += 1
            if new_rottens:
                new_oranges = True
                for orange in new_rottens:
                    rotten.append(orange)
        # check for unreachable fresh oranges
        if len(to_visit) > 0:
            return -1
        else:
            return time