# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1, l2):
        head_ptr = None
        node = None
        carry = 0
        while l1 is not None or l2 is not None:
            # handle case of first iteration
            if head_ptr is None:
                head_ptr = ListNode()
                node = head_ptr
            # handle subsequent iteration
            else:
                node.next = ListNode()
                node = node.next
            # process data in LLs
            if l1 is None:
                sum = carry + l2.val
                l2 = l2.next
            elif l2 is None:
                sum = carry + l1.val
                l1 = l1.next
            else:
                sum = carry + l1.val + l2.val
                l1 = l1.next
                l2 = l2.next
            # handle case of carry
            if sum > 9:
                carry = 1
            else:
                carry = 0
            node.val = sum % 10
        # handle case of final carry
        if carry == 1:
            node.next = ListNode()
            node.next.val = 1
        # return head to calling function
        return head_ptr