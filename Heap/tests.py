# Author: Donald Logan Kiser
# Date: 01/01/2022
# Description: unit testing for implementation of MaxHeap

import unittest
from MaxHeap import MaxHeap

class MaxHeapTests(unittest.TestCase):
    def test_1(self):
        arr = [10, 20, 25, 6, 12, 15, 4, 16]
        h = MaxHeap(len(arr), arr)
        heapified = [25, 20, 15, 16, 12, 10, 4, 6]
        self.assertEqual(h.heap, heapified)

    # def test_2(self):
    #     sol = Solution()
    #     s = '226'
    #     output = 3
    #     self.assertEqual(sol.numDecodings(s), output)
    
    # def test_3(self):
    #     sol = Solution()
    #     s = '06'
    #     output = 0
    #     self.assertEqual(sol.numDecodings(s), output)

    # def test_4(self):
    #     # sol = Solution()
    #     # s = '12'
    #     # output = 2
    #     # self.assertEqual(sol.numDecodings(s), output)
    #     pass


if __name__ == '__main__':
    unittest.main()