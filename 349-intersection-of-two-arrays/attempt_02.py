class Solution:
    def intersection(self, nums1, nums2):
        # get arrays in terms of largest/smallest
        smaller, larger = nums1, nums2
        if len(nums1) > len(nums2):
            smaller, larger = larger, smaller
        # process elements of smaller into set
        helper = set()
        for num in smaller:
            if num not in helper:
                helper.add(num)
        # loop through nums in larger array, building intersection
        res = set()
        i = 0
        while i < len(larger) and len(res) < len(helper):
            if larger[i] in helper:
                if larger[i] not in res:
                    res.add(larger[i])
            i += 1
        return list(res)
