# Author: Donald Logan Kiser
# Date: 12/26/2021
# Problem: leetcode #518 coin change II
# Description: unit testing

import unittest
from attempt_01_bottom_up import Solution

class CoinChangeTests(unittest.TestCase):
    def test_1(self):
        sol = Solution()
        coins = [1, 2, 5]
        amount = 5
        output = 4
        self.assertEqual(sol.change(amount, coins), output)

    def test_2(self):
        sol = Solution()
        coins = [2]
        amount = 3
        output = 0
        self.assertEqual(sol.change(amount, coins), output)
    
    def test_3(self):
        sol = Solution()
        coins = [10]
        amount = 10
        output = 1
        self.assertEqual(sol.change(amount, coins), output)

    def test_4(self):
        # sol = Solution()
        # coins = [1, 2, 5]
        # amount = 5
        # output = 4
        # self.assertEqual(sol.change(amount, coins), output)
        pass


if __name__ == '__main__':
    unittest.main()