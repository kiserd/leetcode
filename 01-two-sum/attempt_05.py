class Solution:
    def twoSum(self, nums, target: int):
        visited = {}
        for idx, num in enumerate(nums):
            if num in visited:
                return [visited[num], idx]
            visited[target - num] = idx
