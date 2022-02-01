class Solution:
    def allPathsSourceTarget(self, graph):
        # define recursive dfs function
        def dfs(path):
            # handle successful base case
            if path[len(path) - 1] == len(graph) - 1:
                return [path]
            # handle unsuccessful base case
            adjs = graph[path[len(path) - 1]]
            if not adjs:
                return []
            # handle recursive exploration
            res = []
            for adj in adjs:
                for rec in dfs(path + [adj]):
                    res.append(rec)
            return res
        # kick off function
        return dfs([0])
