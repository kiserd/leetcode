import unittest
from longest_common_contiguous_subsequence import lccs

class lccs_tests(unittest.TestCase):
    """
    definte unit tests for dynamic_array.py
    """
    def test_1(self):
        """
        test #1
        """
        user0 = ['/page', 'red', 'pink', 'register', 'orange', 'green', 'silly', 'extra']
        user1 = ['/page', 'extra', 'green', 'pink', 'register', 'orange', 'silly']
        res = lccs(user0, user1)
        self.assertEqual(res, ['pink', 'register', 'orange'])




if __name__ == '__main__':
    unittest.main()