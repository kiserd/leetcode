import heapq
class Solution:
    def findKthLargest(self, nums, k: int) -> int:
        # give elements of num opposite sign, to work with heapq minheap
        for i in range(len(nums)):
            nums[i] = -nums[i]
        # heapify the array in linear time
        heapq.heapify(nums)
        # pop k-1 elements off the heap
        for i in range(k - 1):
            heapq.heappop(nums)
        # return the kth element
        return -heapq.heappop(nums)