class Solution:
    def findLength(self, nums1, nums2) -> int:
        # define a couple helper variables
        m = len(nums1)
        n = len(nums2)
        # build memo array
        memo = [[0] * (n + 1) for _ in range(m + 1)]
        # iterate through m x n possible array suffix "starts"
        res = 0
        max_array = []
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                # handle case of equal chars
                if nums1[i] == nums2[j]:
                    memo[i][j] = 1 + memo[i + 1][j + 1]
                    if memo[i][j] > res:
                        res = memo[i][j]
                        max_array = nums1[i:i+memo[i][j]]
                # handle case of unequal chars
                else:
                    memo[i][j] = 0
        return res
