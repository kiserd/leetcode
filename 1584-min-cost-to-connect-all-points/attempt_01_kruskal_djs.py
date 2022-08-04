# utilizing Kruskal's Algorithm
class Solution:
    def minCostConnectPoints(self, points) -> int:
        # define a couple helper variables
        n = len(points)
        e = Edges(points)
        ds = DisjointSet(n)
        num_edges = 0
        dist = 0
        # loop through edges in ascending order
        for i in range(len(e.edges)):
            if num_edges == n - 1:
                return dist
            if ds.root[e.edges[i].idx[0]] != ds.root[e.edges[i].idx[1]]:
                ds.union(e.edges[i].idx[0], e.edges[i].idx[1])
                dist += e.edges[i].dist
                num_edges += 1
        return dist


class Edges:
    def __init__(self, points):
        # process edges
        arr = []
        for i in range(len(points)):
            for j in range(i + 1, len(points), 1):
                edge = Edge(i, points[i], j, points[j])
                arr.append(edge)
        arr.sort(key=lambda edge: edge.dist)
        self.edges = arr


class Edge:
    def __init__(self, idx1, coord1, idx2, coord2):
        self.idx = [idx1, idx2]
        self.dist = abs(coord1[0] - coord2[0]) + abs(coord1[1] - coord2[1])


class DisjointSet:
    def __init__(self, n):
        self.root = [i for i in range(n)]
        self.rank = [1] * n

    def find(self, i):
        # handle base case of root
        if i == self.root[i]:
            return i
        # set root to recursive exploration of parent's root
        self.root[i] = self.find(self.root[self.root[i]])
        # return result of recursive exploration
        return self.root[i]

    def union(self, i, j):
        # get roots
        root_i = self.find(i)
        root_j = self.find(j)
        # only process if roots are different
        if root_i != root_j:
            if self.rank[root_i] > self.rank[root_j]:
                self.root[root_j] = self.root[root_i]
                for k in range(len(self.root)):
                    if self.root[k] == root_j:
                        self.find(k)
                        # self.root[k] == root_i
            elif self.rank[root_j] > self.rank[root_i]:
                self.root[root_i] = self.root[root_j]
                for k in range(len(self.root)):
                    if self.root[k] == root_i:
                        self.find(k)
                        # self.root[k] = root_j
            else:
                self.root[root_j] = self.root[root_i]
                self.rank[i] += 1
                for k in range(len(self.root)):
                    if self.root[k] == root_j:
                        self.find(k)
                        # self.root[k] == root_i

    # def numConnectedComponents(self):
    #     roots = []
    #     num = 0
    #     for i in self.root:
    #         root = self.find(i)
    #         if root not in roots:
    #             roots.append(root)
    #             num += 1
    #     return num
