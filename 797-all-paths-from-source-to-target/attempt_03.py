# make an attempt at dp
class Solution:
    def allPathsSourceTarget(self, graph):
        # define recursive dfs function
        def dfs(path, i):
            # handle successful base case
            if memo[i] is not None and memo[i] is not False:
                return path + [memo[i]]
            # handle unsuccessful base case
            adjs = graph[i]
            if not adjs:
                memo[i] = False
                return False
            # handle recursive exploration
            res = []
            for adj in adjs:
                for rec in dfs(path + [adj]):
                    res.append(rec)
            return res
        # define memo array and kick off function
        memo = [None] * len(graph)
        memo[len(graph) - 1] = []
        return dfs([0])
