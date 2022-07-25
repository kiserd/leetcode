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
        while l1 and l2:
            curr.next = ListNode()
            curr = curr.next
            sum = l1.val + l2.val + carry
            if sum > 9:
                carry = 1
                curr.val = sum - 10
            else:
                carry = 0
                curr.val = sum
            # process ll's for next elt
            l1 = l1.next
            l2 = l2.next
        # handle case of l1 or l2 having remaining nodes
        if l1 or l2:
            ll = l1
            if l2:
                ll = l2
            while ll:
                curr.next = ListNode()
                curr = curr.next
                sum = ll.val + carry
                if sum > 9:
                    carry = 1
                    curr.val = sum - 10
                else:
                    carry = 0
                    curr.val = sum
                ll = ll.next
        return head.next
        


