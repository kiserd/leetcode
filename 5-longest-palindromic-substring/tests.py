# Author: Donald Logan Kiser
# Date: 08/13/2021
# Problem: leetcode #5 longest palindromic substring
# Description: unit testing

import unittest
from attempt_3 import Solution

class longtestPalindromeTests(unittest.TestCase):
    def test_1(self):
        sol = Solution()
        s = "bab"
        sol = Solution()
        self.assertEqual(sol.longestPalindrome(s), "bab")

    def test_2(self):
        s = "cbbd"
        sol = Solution()
        self.assertEqual(sol.longestPalindrome(s), "bb")
    
    def test_3(self):
        s = "a"
        sol = Solution()
        self.assertEqual(sol.longestPalindrome(s), "a")

    def test_4(self):
        s = "aaaaaaaaaaaaaaaaaa"
        sol = Solution()
        self.assertEqual(sol.longestPalindrome(s), "aaaaaaaaaaaaaaaaaa")


if __name__ == '__main__':
    unittest.main()