class Solution:
    def findCircleNum(self, isConnected) -> int:
        # prepare data structures to track disjoint set
        n = len(isConnected)
        root = [i for i in range(n)]
        # rank = [1] * n
        res = n

        # define a couple helper functions
        def union(i, j):
            if root[i] != root[j]:
                root[root[j]] = root[i]

        def set_roots(i):
            # handle base case
            if root[i] == i:
                return i
            # handle recursive exploration
            root[i] = set_roots(root[i])
            return root[i]

        # kick off processing
        for i in range(n):
            for j in range(n):
                if i != j and isConnected[i][j]:
                    set_roots(i)
                    set_roots(j)
                    if root[i] != root[j]:
                        union(i, j)
                        res -= 1
        return res
