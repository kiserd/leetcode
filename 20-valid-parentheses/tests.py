# Author: Donald Logan Kiser
# Date: 08/12/2021
# Description: unit testing for leetcode valid parentheses problem

import unittest
from attempt_1 import Solution

class validParenTests(unittest.TestCase):
    def test_1(self):
        s = "()"
        sol = Solution()
        self.assertTrue(sol.isValid(s))

    def test_2(self):
        s = "()[]{}"
        sol = Solution()
        self.assertTrue(sol.isValid(s))
    
    def test_3(self):
        s = "(]"
        sol = Solution()
        self.assertFalse(sol.isValid(s))


if __name__ == '__main__':
    unittest.main()