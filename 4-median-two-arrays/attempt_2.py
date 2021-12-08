# Author: Donald Logan Kiser
# Date: 07/04/2021
# Description: attempt to solve problems using the following video as guidance
#              https://www.youtube.com/watch?v=LPFhl65R7ww
#
#              attempt to partition both arrays s.t. no element in either left
#              component is greater than any element in the right component(s)
#              and the combined left/right partitions are equal in size
#
#              should be O(log(m + n))

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        # let nums1 ALWAYS represent the shortest array
        if len(nums2) < len(nums1):
            nums1, nums2 = nums2, nums1

        # create some helper variables
        len1 = len(nums1)
        # print("len1 = {0}".format(len1))
        len2 = len(nums2)
        # print("len2 = {0}".format(len2))
        even_len = (len1 + len2) % 2 == 0

        # get size of combined left partition
        # if odd number elements, left slize will be larger by one element
        left_slice_size = (len1 + len2) // 2
        if not even_len:
            left_slice_size += 1
        right_slice_size = len1 + len2 - left_slice_size
        # print("left_slice_size = {0}".format(left_slice_size))
        # print("right_slice_size = {0}".format(right_slice_size))

        # these indices will track the last element in our left partitions
        index1_lo = 0
        index1_hi = len1

        # use binary search on shortest array to find our partition "slice"
        while index1_lo <= index1_hi:
            # get partitioning indices by searching mid of nums1 range
            # print("index1_lo = {}".format(index1_lo))
            # print("index1_hi = {}".format(index1_hi))
            index1_mid = ((index1_hi - index1_lo) // 2) + index1_lo
            # print("index1_mid = {}".format(index1_mid))
            index2 = left_slice_size - index1_mid
            # print("index2 = {}".format(index2))
            # get min and max elts on both sides of partition
            l1 = self.getLeftMax(nums1, index1_mid)
            # print("l1 = {}".format(l1))
            r1 = self.getRightMin(nums1, index1_mid)
            # print("r1 = {}".format(r1))
            l2 = self.getLeftMax(nums2, index2)
            # print("l2 = {}".format(l2))
            r2 = self.getRightMin(nums2, index2)
            # print("r2 = {}".format(r2))
            # handle case where l1 > r2
            if l1 > r2:
                index1_hi = index1_mid - 1
            # handle case where l2 > r1
            elif l2 > r1:
                index1_lo = index1_mid + 1
            else:
                if not even_len:
                    return max(l1, l2)
                else:
                    return (max(l1, l2) + min(r1, r2)) / 2
    
    def getLeftMax(self, nums, index_part):
        if index_part == 0:
            return -(10**8)
        else:
            return nums[index_part - 1]
    
    def getRightMin(self, nums, index_part):
        if index_part == len(nums):
            return 10**8
        else:
            return nums[index_part]
