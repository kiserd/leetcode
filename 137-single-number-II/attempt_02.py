class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # calculate total sum and unique sum
        visited = set()
        unique_sum = 0
        total_sum = 0
        for num in nums:
            if num not in visited:
                unique_sum += num
                visited.add(num)
            total_sum += num
        # 3 * unique_sum - total_sum = 2 * unique_element
        unique_element = (3 * unique_sum - total_sum) // 2
        return unique_element
