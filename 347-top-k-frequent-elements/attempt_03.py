import heapq
class Solution:
    def topKFrequent(self, nums, k: int):
        freqs = {}
        for num in nums:
            freqs[num] = freqs.get(num, 0) - 1
        counts = []
        for key in freqs:
            counts.append((freqs[key], key))
        heapq.heapify(counts)
        res = []
        for _ in range(k):
            res.append(heapq.heappop(counts)[1])
        return res
