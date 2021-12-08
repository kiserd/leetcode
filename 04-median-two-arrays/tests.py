# Author: Donald Logan Kiser
# Date: 07/03/2021
# Description: unit testing for leetcode median of two sorted arrays

import unittest
from attempt_2 import Solution

class MedianTests(unittest.TestCase):
    def test_1(self):
        nums1 = [1, 3]
        nums2 = [2]
        s = Solution()
        self.assertEqual(s.findMedianSortedArrays(nums1, nums2), 2)

    def test_2(self):
        nums1 = [1, 3, 5, 7]
        nums2 = [2, 4, 6]
        s = Solution()
        self.assertEqual(s.findMedianSortedArrays(nums1, nums2), 4)


if __name__ == '__main__':
    unittest.main()