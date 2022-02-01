class Solution:
    def allPathsSourceTarget(self, graph):
        # define variables to be used in processing
        n = len(graph)
        s = [[0, elt] for elt in graph[0]]
        res = []
        # process stack until all paths explored
        while len(s) != 0:
            curr = s.pop()
            adjs = graph[curr[len(curr) - 1]]
            # add to res if destination reached
            if curr[len(curr) - 1] == n - 1:
                res.append(curr)
            # add adjacencies to current list and add to stack
            for adj in adjs:
                s.append(curr + [adj])
        return res


            