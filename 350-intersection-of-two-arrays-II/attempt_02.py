# found clever approach in solution, only need to build on dict
class Solution:
    def intersect(self, nums1, nums2):
        # build dictionaries of counts
        dict1 = {}
        for num in nums1:
            if num not in dict1:
                dict1[num] = 1
            else:
                dict1[num] += 1
        # build array to return to calling function
        arr = []
        for num in nums2:
            if dict1.get(num):
                arr.append(num)
                dict1[num] -= 1
        return arr
