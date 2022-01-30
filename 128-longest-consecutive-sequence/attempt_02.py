# the key to the leetcode solution is that sets are hashed and we only count
# interval length if it is the first in the sequence

# this solution is slower than necessary, should leverage the power of Python
# built-in set, but nice to peek under the hood a bit

class Solution:
    def longestConsecutive(self, nums) -> int:
        helper = {}
        max_lcs = 0
        # get nums in hashable format
        for num in nums:
            helper[num] = None
        # iterate through nums counting interval sizes
        for num in helper.keys():
            if num - 1 not in helper:
                count = 0
                current = num
                while current in helper:
                    count += 1
                    current += 1
                max_lcs = max(max_lcs, count)
        return max_lcs
        