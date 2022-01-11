# this was my 45-min simulated Facebook interview solution. Note, I relied on
# debugging a bit in Leetcode editor
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        min_times = [[100] * len(grid[0]) for i in range(len(grid))]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    print('i: ', i)
                    print('j: ', j)
                    q = [{'time': 0, 'node': [i, j]}]
                    visited = []
                    while len(q) != 0:
                        ##### DEBUG
                        print('beg===========')
                        for row in min_times:
                            print(row)
                        ###########
                        elt = q.pop()
                        time = elt['time']
                        row, col = elt['node']
                        # print('row: ', row)
                        # print('col: ', col)
                        # print('visited: ', visited)
                        if [row, col] not in visited:
                            if min_times[row][col] > time:
                                min_times[row][col] = time
                                print('end===========')
                                for thing in min_times:
                                    print(thing)
                            for node in self.get_adj(row, col, len(grid), len(grid[0])):
                                if node not in visited and grid[node[0]][node[1]] == 1:
                                    q.insert(0, {'time': time + 1, 'node': node})
                            visited.append([row, col])
        final_min_time = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    if min_times[i][j] == 100:
                        return -1
                    if final_min_time < min_times[i][j]:
                        final_min_time = min_times[i][j]
        return final_min_time
                            
    
    
    def get_adj(self, i, j, m, n):
        arr = []
        if i - 1 > -1:
            arr.append([i - 1, j])
        if i + 1 < m:
            arr.append([i + 1, j])
        if j - 1 > -1:
            arr.append([i, j - 1])
        if j + 1 < n:
            arr.append([i, j + 1])
        return arr