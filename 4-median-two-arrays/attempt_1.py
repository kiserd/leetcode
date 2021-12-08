# Author: Donald Logan Kiser
# Date: 08/25/2020
# Description: first attempt at the problem. Intentionally not 'over-thinking'
#              things. Just trying to get familiar with the problem via dumb
#              blind tinkering.
#
#              given len(nums1) = n and len(nums2), this solution will most
#              likely be O(m+n) at best

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        # create a couple helper vars to make code more readable
        len1 = len(nums1)                               # O(n)
        len2 = len(nums2)                               # O(m)
        len_total = len1 + len2
        avg_of_two = len_total % 2 == 0
        index1 = 0
        index2 = 0
        new_list = []
        # merge lists
        while index1 < len1 or index2 < len2:           # O(m + n)
            if index1 == len1:
                new_list.append(nums2[index2])
                index2 += 1
            elif index2 == len2:
                new_list.append(nums1[index1])
                index1 += 1
            elif nums1[index1] < nums2[index2]:
                new_list.append(nums1[index1])
                index1 += 1
            else:
                new_list.append(nums2[index2])
                index2 += 1
        
        # find median
        if avg_of_two:
            elt1 = new_list[(len_total // 2) - 1]
            elt2 = new_list[len_total // 2]
            return (elt1 + elt2) / 2
        else:
            return new_list[len_total // 2]
