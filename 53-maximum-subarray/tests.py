# Author: Donald Logan Kiser
# Date: 12/29/2021
# Problem: leetcode #53 maximum subarray
# Description: unit testing

import unittest
from attempt_01_bottom_up import Solution

class MaxSubarrayTests(unittest.TestCase):
    def test_1(self):
        sol = Solution()
        nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
        output = 6
        self.assertEqual(sol.maxSubArray(nums), output)


if __name__ == '__main__':
    unittest.main()