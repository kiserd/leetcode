import heapq
class Solution:
    def topKFrequent(self, nums, k: int):
        # build dict that tracks counts
        dict = {}
        for num in nums:
            if num in dict:
                dict[num] += 1
            else:
                dict[num] = 1
        # heapify dict and get k largest
        return heapq.nlargest(k, dict.keys(), key = lambda key: dict[key])
