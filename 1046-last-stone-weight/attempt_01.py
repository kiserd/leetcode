from typing import List
import heapq


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        h = []
        for stone in stones:
            heapq.heappush(h, -1 * stone)
        # process stones until less than 2 stones left
        while len(h) > 1:
            fst = -1 * heapq.heappop(h)
            scd = -1 * heapq.heappop(h)
            if fst > scd:
                heapq.heappush(h, -1 * (fst - scd))
        # return result to user / calling function
        if not h:
            return 0
        return -1 * heapq.heappop(h)
