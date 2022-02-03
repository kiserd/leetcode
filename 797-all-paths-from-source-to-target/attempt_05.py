# solve recursively, without dp
class Solution:
    def allPathsSourceTarget(self, graph):
        # define recursive function
        def bfs(i):
            # handle base case
            if i == len(graph) - 1:
                return [[i]]
            # handle recursive exploration
            res = []
            for adj in graph[i]:
                for path in bfs(adj):
                    res.append([i] + path)
            return res
        # kick off function
        return bfs(0)