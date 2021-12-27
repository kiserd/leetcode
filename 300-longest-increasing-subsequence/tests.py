# Author: Donald Logan Kiser
# Date: 12/26/2021
# Problem: leetcode #300 longest increasing subsequence
# Description: unit testing

import unittest
from attempt_01_top_down import Solution

class LISTests(unittest.TestCase):
    def test_1(self):
        sol = Solution()
        nums = [10, 9, 2, 5, 3, 7, 101, 18]
        output = 4
        self.assertEqual(sol.lengthOfLIS(nums), output)

    def test_2(self):
        sol = Solution()
        nums = [0, 1, 0, 3, 2, 3]
        output = 4
        self.assertEqual(sol.lengthOfLIS(nums), output)
    
    def test_3(self):
        sol = Solution()
        nums = [7, 7, 7, 7, 7, 7, 7]
        output = 1
        self.assertEqual(sol.lengthOfLIS(nums), output)

    def test_4(self):
        sol = Solution()
        nums = [4, 10, 4, 3, 8, 9]
        output = 3
        self.assertEqual(sol.lengthOfLIS(nums), output)


if __name__ == '__main__':
    unittest.main()