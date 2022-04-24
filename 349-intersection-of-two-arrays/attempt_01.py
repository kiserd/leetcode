class Solution:
    def intersection(self, nums1, nums2):
        # iterate through smallest array, noting uniques
        helper = {}
        res = []
        for num in nums1:
            helper[num] = 0
        for num in nums2:
            if num in helper and not helper[num]:
                res.append(num)
                helper[num] += 1
        return res
