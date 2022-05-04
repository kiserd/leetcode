# Author:       Donald Logan Kiser
# Date:         05/03/2022
# Description:  working through problem that stumped me during Karat interview
#               NOTE: this should be handled "bottom-up" see lc problem 718,
#                     the top down implementation gets TLE

# user0 = ['/page', 'red', 'pink', 'register', 'orange', 'green', 'silly', 'extra']
# user1 = ['/page', 'extra', 'green', 'pink', 'register', 'orange', 'silly']


def lccs(arr1, arr2):
    # build memo array
    memo = [[None] * len(arr2) for _ in range(len(arr1))]
    # define recursive helper function
    def dp(i, j):
        # handle base case
        if i == len(arr1) or j == len(arr2):
            return 0
        # handle recursive exploration
        if memo[i][j] is None:
            # handle case of equal element
            if arr1[i] == arr2[j]:
                memo[i][j] = 1 + dp(i + 1, j + 1)
            else:
                memo[i][j] = 0
                # kick off exploration
                dp(i + 1, j)
                dp(i, j + 1)
        return memo[i][j]
    # kick off function to build out memo
    dp(0, 0)
    # search memo for longest common contiguous subsequence, return to user
    max_len = -1
    res = []
    for i in range(len(arr1)):
        for j in range(len(arr2)):
            if memo[i][j] and memo[i][j] > max_len:
                max_len = memo[i][j]
                res = arr1[i:i+memo[i][j]]
    return res
