# top-down
# attempt using lru_cache as a crutch
from functools import lru_cache
class Solution:
    def lengthOfLIS(self, nums) -> int:
        global outer
        # define recursive function
        def dp(i):
            '''
            DESCRIPTION:    determines LIS for subsequence ending with the ith
                            element

            INPUT:          i (int): index of the ending element of the
                                     subsequence

            RETURN:         LIS for subsequence ending with the ith element
            '''
            global outer
            print(f'i: {i}')
            # loop through next possible elements
            max_lcs = 1
            for j in range(i - 1 , -1, -1):
                print(f'j: {j}')
                if nums[j] < nums[i]:
                    print(f'calling dp(${j})')
                    max_lcs = max(max_lcs, dp(j) + 1)
                else:
                    dp(j)
            # update memo and return to calling function
            if max_lcs > outer:
                outer = max_lcs
            return max_lcs
            
        outer = 0
        # call recursive function from beginning of array
        dp(len(nums) - 1)
        return outer