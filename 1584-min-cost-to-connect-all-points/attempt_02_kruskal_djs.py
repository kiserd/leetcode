# kruskals via disjoint set
from typing import List
import heapq


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # add all possible edges to min-heap
        edges = []
        for i in range(len(points)):
            for j in range(i, len(points)):
                h_dist = abs(points[i][0] - points[j][0])
                v_dist = abs(points[i][1] - points[j][1])
                heapq.heappush(edges, (h_dist + v_dist, i, j))
        # init disjoint set
        djs = DisjointSet(len(points))
        cost = 0
        while djs.num > 1:
            wt, i, j = heapq.heappop(edges)
            if not djs.is_connected(i, j):
                djs.union(i, j)
                cost += wt
        return cost


class DisjointSet():

    def __init__(self, sz):
        self.root = [i for i in range(sz)]
        self.num = sz

    def get_root(self, a):
        # handle base case
        if self.root[a] == a:
            return a
        # handle recursive exploration
        self.root[a] = self.get_root(self.root[a])
        return self.root[a]

    def union(self, a, b):
        # first get roots
        root_a = self.get_root(a)
        root_b = self.get_root(b)
        # handle unioning
        if root_a != root_b:
            self.root[root_a] = root_b
        self.num -= 1

    def is_connected(self, a, b):
        self.get_root(a)
        self.get_root(b)
        return self.root[a] == self.root[b]
