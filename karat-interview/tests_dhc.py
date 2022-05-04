import unittest
from attempt_02 import ListNode, addTwoNumbers

class lccs_tests(unittest.TestCase):
    """
    definte unit tests for dynamic_array.py
    """
    def test_1(self):
        """
        test #1
        """
        l1 = ListNode()
        l1.next = ListNode()
        l1.next.next = ListNode()
        l1.val = 2
        l1.next.val = 2
        l1.next.next.val = 1

        l2 = ListNode()
        l2.next = ListNode()
        l2.next.next = ListNode()
        l2.val = 1
        l2.next.val = 1
        l2.next.next.val = 1

        l3 = addTwoNumbers(l1, l2)
        print(l3.val)
        print(l3.next.val)
        print(l3.next.next.val)



if __name__ == '__main__':
    unittest.main()