# Author: Donald Logan Kiser
# Date: 01/03/2022
# Description: unit testing for implementation of quicksort

import unittest
from quicksort import quicksort, partition

class QuicksortTests(unittest.TestCase):
    def test_1(self):
        arr = [10, 20, 25, 6, 12, 15, 4, 16]
        output = [4, 6, 10, 12, 15, 16, 20, 25]
        quicksort(arr, 0, len(arr) - 1)
        self.assertEqual(arr, output)

    def test_2(self):
        arr = []
        output = []
        quicksort(arr, 0, len(arr) - 1)
        self.assertEqual(arr, output)
    
    def test_3(self):
        arr = [1]
        output = [1]
        quicksort(arr, 0, len(arr) - 1)
        self.assertEqual(arr, output)


if __name__ == '__main__':
    unittest.main()