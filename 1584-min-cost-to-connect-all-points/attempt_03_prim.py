# Prim's algorithm
from typing import List
import heapq


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # define helper function to get distances
        def get_dists(bg, eds):
            res = []
            for ed in eds:
                x_dist = abs(points[bg][0] - points[ed][0])
                y_dist = abs(points[bg][1] - points[ed][1])
                res.append((x_dist + y_dist, bg, ed))
            return res

        # utilize set data struct to keep track of nodes to add to MST
        to_add = set([i for i in range(len(points))])
        # start with 0th point (arbitrarily)
        to_add.remove(0)
        edges = get_dists(0, to_add)
        heapq.heapify(edges)
        total_weight = 0
        while to_add:
            wt, bg, ed = heapq.heappop(edges)
            if ed in to_add:
                total_weight += wt
                to_add.remove(ed)
                for new in get_dists(ed, to_add):
                    heapq.heappush(edges, new)
        return total_weight
