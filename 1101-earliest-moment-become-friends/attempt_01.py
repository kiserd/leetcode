class Solution:
    def earliestAcq(self, logs, n: int) -> int:
        # sort logs by ascending timestamp
        logs.sort(key = lambda log: log[0])
        # initialize disjoin set
        ds = DisjointSet(n)
        # loop through logs, unioning friends
        i = 0
        while i < len(logs):
            ds.union(logs[i][1], logs[i][2])
            # handle case where all friends (now) share common root
            if ds.all_friends():
                return logs[i][0]
            i += 1
        # all logs processed, no common root
        return -1

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
    
    def all_friends(self):
        roots = []
        num = 0
        for i in self.root:
            root = self.find(i)
            if root not in roots:
                roots.append(root)
                num += 1
        return len(roots) == 1