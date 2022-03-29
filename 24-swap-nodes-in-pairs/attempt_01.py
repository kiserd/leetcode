# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head):
        # create dummy head
        dummy_head = ListNode(None, head)
        # define recursive function
        def rec(node):
            # handle base case(s)
            if not node.next or not node.next.next:
                return node.next
            # handle recursive case
            fst = node.next.next
            scd = node.next
            scd.next = fst.next
            fst.next = scd
            node.next = fst
            rec(scd)
        rec(dummy_head)
        return dummy_head.next
