class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        unique = set()
        multiple = set()
        for num in nums:
            if num in unique:
                unique.remove(num)
                multiple.add(num)
            elif num not in multiple:
                unique.add(num)
        return list(unique)[0]
