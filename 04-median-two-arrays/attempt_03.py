# Author: Donald Logan Kiser
# Date: 07/04/2021
# Description: optimize attempt_2 and get rid of debug print statements
#              return to this problem later

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        # let nums1 ALWAYS represent the shortest array
        if len(nums2) < len(nums1):
            nums1, nums2 = nums2, nums1

        # create some helper variables
        len1 = len(nums1)
        len2 = len(nums2)
        even_len = (len1 + len2) % 2 == 0

        # get size of combined left partition
        # if odd number elements, left slize will be larger by one element
        left_slice_size = (len1 + len2) // 2
        if not even_len:
            left_slice_size += 1

        # these indices will track the last element in our left partitions
        index1_lo = 0
        index1_hi = len1

        # use binary search on shortest array to find our partition "slice"
        while index1_lo <= index1_hi:
            # get partitioning indices by searching mid of nums1 range
            index1_mid = ((index1_hi - index1_lo) // 2) + index1_lo
            index2 = left_slice_size - index1_mid
            l1 = self.getLeftMax(nums1, index1_mid)
            r1 = self.getRightMin(nums1, index1_mid)
            l2 = self.getLeftMax(nums2, index2)
            r2 = self.getRightMin(nums2, index2)
            # handle case where l1 > r2
            if l1 > r2:
                index1_hi = index1_mid - 1
            # handle case where l2 > r1
            elif l2 > r1:
                index1_lo = index1_mid + 1
            # handle case where we are ready to return our result
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
