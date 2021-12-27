# top-down
# big issues here, moving on
class Solution:
    def lengthOfLIS(self, nums) -> int:
        # define recursive function
        def dp(i):
            '''
            DESCRIPTION:    determines LIS for subsequence ending with the ith
                            element

            INPUT:          i (int): index of the ending element of the
                                     subsequence

            RETURN:         LIS for subsequence ending with the ith element
            '''
            print(f'i: {i}')
            print(f'prior memo: ', memo)
            # handle case where memoized result has been found
            if memo[i] > 0:
                return memo[i]
            # handle case where no memoized result has been found
            else:
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
                memo[i] = max_lcs
                print('after memo: ', memo)
                return memo[i]
            

        # build memo and set base case implicitly in memo
        memo = [0] * len(nums)
        memo[0] = 1
        outter_max = 0
        # call recursive function from beginning of array
        dp(len(nums) - 1)
        return max(memo)