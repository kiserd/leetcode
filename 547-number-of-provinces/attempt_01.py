# exploration specifically instructed user to leverage disjoint
# sets

class Solution:
    def findCircleNum(self, isConnected) -> int:
        # construct DisjointSet object
        ds = DisjointSet(len(isConnected[0]))
        # loop through isConnected, unioning connected cities
        for i in range(len(isConnected)):
            for j in range(i + 1, len(isConnected), 1):
                if isConnected[i][j] == 1 or isConnected[j][i] == 1:
                    ds.union(i, j)
        return ds.numProvinces()

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
            if self.rank[i] > self.rank[j]:
                self.root[root_j] = self.root[root_i]
            elif self.rank[j] > self.rank[i]:
                self.root[root_i] = self.root[root_j]
            else:
                self.root[root_j] = self.root[root_i]
                self.rank[i] += 1
    
    def numProvinces(self):
        roots = []
        num = 0
        for i in self.root:
            root = self.find(i)
            if root not in roots:
                roots.append(root)
                num += 1
        return num
