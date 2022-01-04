import heapq
class Solution:
    def topKFrequent(self, nums, k: int):
        # build dict that tracks counts
        dict = {}
        for num in nums:
            if num in dict:
                dict[num] -= 1
            else:
                dict[num] = -1
        # build array of tuples (count, num)
        arr = []
        for key, val in dict.items():
            arr.append((val, key))
        # heapify array and pop k elements into return list
        heapq.heapify(arr)
        return_list = []
        for i in range(k):
            return_list.append(heapq.heappop(arr)[1])
        return return_list
