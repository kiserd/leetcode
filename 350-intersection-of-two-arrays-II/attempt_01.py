class Solution:
    def intersect(self, nums1, nums2):
        # build dictionaries of counts
        dict1 = {}
        for num in nums1:
            if num not in dict1:
                dict1[num] = 1
            else:
                dict1[num] += 1
        dict2 = {}
        for num in nums2:
            if num not in dict2:
                dict2[num] = 1
            else:
                dict2[num] += 1
        # build array to return to calling function
        arr = []
        small_dict = dict2
        big_dict = dict1
        if len(dict1) < len(dict2):
            small_dict = dict1
            big_dict = dict2
        for key in small_dict:
            if key in big_dict:
                for i in range(min(dict1[key], dict2[key])):
                    arr.append(key)
        return arr
