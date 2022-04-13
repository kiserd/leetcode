class Solution:
    def allPathsSourceTarget(self, graph):
        # build out adjacency dict
        adjs = {i: [] for i in range(len(graph))}
        for i in range(len(graph)):
            for j in graph[i]:
                adjs[i].append(j)
        # work through DFS using stack
        s = [[0]]
        res = []
        while s:
            curr = s.pop()
            for adj in adjs[curr[-1]]:
                if adj == len(graph) - 1:
                    res.append(curr + [adj])
                else:
                    s.append(curr + [adj])
        return res
