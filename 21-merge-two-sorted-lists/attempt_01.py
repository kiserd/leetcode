# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1, list2):
        # define recursive function
        def merge(l1, l2):
            # handle base cases
            if not l1 and not l2:
                return None
            if not l1:
                return l2
            if not l2:
                return l1
            # handle recursive case
            if l1.val < l2.val:
                l1.next = merge(l1.next, l2)
                return l1
            else:
                l2.next = merge(l1, l2.next)
                return l2
        return merge(list1, list2)
