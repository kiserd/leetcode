# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1, l2):
        head = ListNode()
        curr = head
        carry = 0
        while l1 or l2 or carry:
            # attempt to return early
            if (not l1 and not carry) or (not l2 and not carry):
                if l1:
                    curr.next = l1
                    return head.next
                if l2:
                    curr.next = l2
                    return head.next
            curr.next = ListNode()
            curr = curr.next
            val1 = 0
            val2 = 0
            if l1:
                val1 = l1.val
                l1 = l1.next
            if l2:
                val2 = l2.val
                l2 = l2.next
            sum = val1 + val2 + carry
            curr.val = sum % 10
            carry = sum // 10
        return head.next
