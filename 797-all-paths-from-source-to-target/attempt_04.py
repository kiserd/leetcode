# implemented with my dummy queue that is space-inefficient
class Solution:
    def allPathsSourceTarget(self, graph):
        # process nodes in a bfs manner via queue
        q = [[0]]
        next = 0
        res = []
        while next < len(q):
            curr = q[next]
            last = curr[len(curr) - 1]
            if last == len(graph) - 1:
                res.append(curr)
            else:
                for adj in graph[curr[len(curr) - 1]]:
                    q.append(curr + [adj])
            next += 1
        return res
                



