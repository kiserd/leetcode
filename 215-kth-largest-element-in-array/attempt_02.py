# after reading through heapq docs, I noticed this was a viable plan of attack.
# However, I thought it would be better to (initially) spell out the process
# using the traditional heap operations
import heapq
class Solution:
    def findKthLargest(self, nums, k: int) -> int:
        return heapq.nlargest(k, nums)[-1]