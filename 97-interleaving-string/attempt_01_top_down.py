class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # handle edge case
        if len(s1) + len(s2) != len(s3): return False
        # define recursive function
        def dp(i, j):
            # return memoized result, if it exists
            if (i, j) in memo: return memo[(i, j)]
            # explore case where we use char from s1
            if i < len(s1) and s1[i] == s3[i + j]:
                if dp(i + 1, j):
                    memo[(i, j)] = True
                    return True
            # explore case where we use char from s2
            if j < len(s2) and s2[j] == s3[i + j]:
                if dp(i, j + 1):
                    memo[(i, j)] = True
                    return True
            # handle neither recursive exploration successful
            memo[(i, j)] = False
            return False
        # define memo with implicit base case and kick off function
        memo = {}
        memo[(len(s1), len(s2))] = True
        return dp(0, 0)
        