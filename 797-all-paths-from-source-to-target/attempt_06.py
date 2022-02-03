# solve recursively, with dp
class Solution:
    def allPathsSourceTarget(self, graph):
        # define recursive function
        def bfs(i):
            # handle base case
            if memo[i]:
                return memo[i]
            # handle recursive exploration
            res = []
            for adj in graph[i]:
                for path in bfs(adj):
                    res.append([i] + path)
            memo[i] = res
            return res
        # define memo, kick off function
        n = len(graph)
        memo = [None] * n
        memo[n - 1] = [[n - 1]]
        return bfs(0)
