from collections import deque
class Solution:
    def getFood(self, grid) -> int:
        # build sets of cells to_visit
        to_visit = set()
        food = set()
        q = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 'O':
                    to_visit.add((i, j))
                elif grid[i][j] == '#':
                    food.add((i, j))
                elif grid[i][j] == '*':
                    q.append((i, j))
        # process q until empty or food is found
        dist = 0
        while q:
            new_q = []
            while q:
                i, j = q.pop()
                # handle food hit
                if (i, j) in food:
                    return dist
                adjs = [(i + 1, j), (i - 1, j), (i, j + 1), (i, j -1)]
                for r, c in adjs:
                    if (r, c) in to_visit or (r, c) in food:
                        new_q.append((r, c))
            q = new_q
            dist += 1
        # food not found, bfs exhausted
        return -1
            
