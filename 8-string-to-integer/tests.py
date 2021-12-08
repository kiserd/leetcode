# Author: Donald Logan Kiser
# Date: 08/12/2021
# Description: unit testing for leetcode string to integer

import unittest
from attempt_2 import Solution

class myAtoiTests(unittest.TestCase):
    def test_1(self):
        s = "42"
        sol = Solution()
        self.assertEqual(sol.myAtoi(s), 42)

    def test_2(self):
        s = "   -42"
        sol = Solution()
        self.assertEqual(sol.myAtoi(s), -42)


if __name__ == '__main__':
    unittest.main()