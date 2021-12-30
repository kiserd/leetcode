# Author: Donald Logan Kiser
# Date: 12/29/2021
# Problem: leetcode #91 decode ways
# Description: unit testing

import unittest
from attempt_01_bottom_up import Solution

class DecodeTests(unittest.TestCase):
    def test_1(self):
        sol = Solution()
        s = '12'
        output = 2
        self.assertEqual(sol.numDecodings(s), output)

    def test_2(self):
        sol = Solution()
        s = '226'
        output = 3
        self.assertEqual(sol.numDecodings(s), output)
    
    def test_3(self):
        sol = Solution()
        s = '06'
        output = 0
        self.assertEqual(sol.numDecodings(s), output)

    def test_4(self):
        # sol = Solution()
        # s = '12'
        # output = 2
        # self.assertEqual(sol.numDecodings(s), output)
        pass


if __name__ == '__main__':
    unittest.main()