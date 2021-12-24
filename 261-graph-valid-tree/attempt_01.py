# spec specifically instructs user to utilize disjoint set data struct
class Solution:
    def validTree(self, n: int, edges) -> bool:
        # loop through edges, building disjoint set
        ds = DisjointSet(n)
        for edge in edges:
            ds.union(edge[0], edge[1])
            if ds.has_cycle:
                return False
        # check if DisjointSet represents a tree
        if not ds.is_tree():
            return False
        # all tests passed, return True
        return True

class DisjointSet:
    def __init__(self, n):
        self.root = [i for i in range(n)]
        self.rank = [1] * n
        self.has_cycle = False
    
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
        else:
            self.has_cycle = True
    
    def is_tree(self):
        # recursively update root[0] because loop misses it
        self.find(0)
        for i in range(1, len(self.root), 1):
            root = self.find(i)
            if root != self.root[i - 1]:
                return False
        return True