# Author: Donald Logan Kiser
# Date: 12/26/2021
# Problem: leetcode #188 when to buy and sell stock
# Description: unit testing

import unittest
from attempt_02_top_down import Solution

class StockTests(unittest.TestCase):
    def test_1(self):
        sol = Solution()
        prices = [2, 4, 1]
        k = 2
        output = 2
        self.assertEqual(sol.maxProfit(k, prices), output)

    def test_2(self):
        sol = Solution()
        prices = [3, 2, 6, 5, 0, 3]
        k = 2
        output = 7
        self.assertEqual(sol.maxProfit(k, prices), output)
    
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