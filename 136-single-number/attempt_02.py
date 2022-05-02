class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        helper = set()
        for num in nums:
            if num in helper:
                helper.remove(num)
            else:
                helper.add(num)
        return list(helper)[0]
