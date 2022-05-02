class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # get unique sum and total sum of nums
        visited = set()
        unique_sum = 0
        total_sum = 0
        for num in nums:
            if num not in visited:
                unique_sum += num
                visited.add(num)
            total_sum += num
        # unique_elt = (2 * unique_sum - total_sum)
        return 2 * unique_sum - total_sum
