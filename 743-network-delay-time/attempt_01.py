# utilize Dijkstra's Algorithm
class Solution:
    def networkDelayTime(self, times, n: int, k: int) -> int:
        # initialize a couple helper variables
        adj = self.build_adj_matrix(n, times)
        unexplored = [i for i in range(1, n + 1, 1)]
        t = [101 for i in range(0, n + 1, 1)]
        t[k] = 0
        # explore until unexplored is empty
        while len(unexplored) > 0:
            # explore vertex at minimum distance first
            v = self.get_min_time(t, unexplored)
            unexplored.remove(v)
            # get adjacencies and weights for chosen vertex
            for end, time in adj[v]:
                # handle case where relaxation is needed
                if t[v] + time < t[end]:
                    t[end] = time + t[v]
        # remove the dummy 0th element
        t.pop(0)
        # handle case of unreachable vertices
        if max(t) > 100:
            return -1
        return max(t)
    
    def get_min_time(self, t, unexplored):
        # set current low to 0th element to assure others are lower
        low = t[unexplored[0]]
        idx_min = unexplored[0]
        for idx in unexplored:
            # handle case of finding a new min
            if t[idx] < low:
                idx_min = idx
                low = t[idx]
        return idx_min
    
    def build_adj_matrix(self, n, times):
        adj = [[] for i in range(n + 1)]
        for start, end, time in times:
            adj[start].append([end, time])
        return adj
