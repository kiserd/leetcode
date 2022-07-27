# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head):
        # handle edge case
        if not head:
            return head
        # get reference to end of list and head of remainder
        new_head = head
        rem = head.next

        def helper(end, rem):
            # handle base case
            if not rem:
                return end
            # handle recursive case
            new_rem = rem.next
            rem.next = end
            return helper(rem, new_rem)
        # turn head into tail
        head.next = None
        return helper(new_head, rem)
