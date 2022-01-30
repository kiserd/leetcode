# disjoint set feels appropriate here, but the root and rank arrays would
# get out of control. Maybe utilizing a hash map would help keep space down

class Solution:
    def longestConsecutive(self, nums) -> int:
        helper = {}
        max_lcs = 0
        for num in nums:
            if num not in helper:
                helper[num] = [num]
                # handle unioning with potential neighbors to the right
                if num + 1 in helper:
                    helper[num] += helper[num + 1]
                    helper[helper[num][len(helper[num]) - 1]] = helper[num]
                # handle unioning with potential neighbors to the left
                if num - 1 in helper:
                    helper[num] = helper[num - 1] + helper[num]
                    helper[helper[num][0]] = helper[num]
                    helper[helper[num][len(helper[num]) - 1]] = helper[num]
                # update our max, if applicable
                max_lcs = max(max_lcs, len(helper[num]))
        return max_lcs
