# Author: Donald Logan Kiser
# Date: 12/27/2021
# Problem: leetcode #309 when to buy and sell stock with cooldown
# Description: unit testing

import unittest
from attempt_01_top_down import Solution

class StockTests(unittest.TestCase):
    def test_1(self):
        sol = Solution()
        prices = [1, 2, 3, 0, 2]
        output = 3
        self.assertEqual(sol.maxProfit(prices), output)

    def test_2(self):
        sol = Solution()
        prices = [1]
        output = 0
        self.assertEqual(sol.maxProfit(prices), output)
    
    # def test_3(self):
    #     sol = Solution()
    #     prices = [2, 4, 1]
    #     k = 2
    #     output = 2
    #     self.assertEqual(sol.maxProfit(k, prices), output)

    # def test_4(self):
    #     sol = Solution()
    #     prices = [2, 4, 1]
    #     k = 2
    #     output = 2
    #     self.assertEqual(sol.maxProfit(k, prices), output)


if __name__ == '__main__':
    unittest.main()