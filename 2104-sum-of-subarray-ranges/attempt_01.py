class Solution:
    def subArrayRanges(self, nums) -> int:
        # get subarray minimums
        A_min = [None] * len(nums)
        s = []
        for i, num in enumerate(nums):
            # find 'most recent' smaller num in stack
            while s and nums[s[-1]] > num:
                s.pop()
            # get index of most recent smallest, handling empty stack
            j = None
            if not s:
                j = -1
                A_min[i] = num * (i - j)
            else:
                j = s[-1]
                A_min[i] = A_min[j] + num * (i - j)
            s.append(i)
        
        # get subarray maximums
        A_max = [None] * len(nums)
        s = []
        for i, num in enumerate(nums):
            # find 'most recent' smaller num in stack
            while s and nums[s[-1]] < num:
                s.pop()
            # get index of most recent smallest, handling empty stack
            j = None
            if not s:
                j = -1
                A_max[i] = num * (i - j)
            else:
                j = s[-1]
                A_max[i] = A_max[j] + num * (i - j)
            s.append(i)
        # solution should be difference of subarray max and mins
        return sum(A_max) - sum(A_min)
