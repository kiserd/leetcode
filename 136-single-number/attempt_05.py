class Solution:
    def singleNumber(self, nums):
        visited = set()
        unique_sum = 0
        total_sum = 0
        for num in nums:
            if num not in visited:
                visited.add(num)
                unique_sum += num
            total_sum += num
        return (2 * unique_sum) - total_sum
