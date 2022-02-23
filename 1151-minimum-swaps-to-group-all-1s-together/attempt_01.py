class Solution:
    def minSwaps(self, data) -> int:
        # handle edge case
        if len(data) == 1: return 0
        # count up the '1's in array
        ones = sum(data)
        if not ones: return 0
        # two pointer processing
        ones_prior = 0
        ones_rem = ones - sum(data[:ones - 1])
        j = ones - 1
        i = 0
        min_swaps = ones_rem
        while j < len(data):
            if data[j]:
                ones_rem -= 1
            min_swaps = min(min_swaps, ones_rem + ones_prior)
            if data[i]:
                ones_prior += 1
            i += 1
            j += 1
        return min_swaps
        