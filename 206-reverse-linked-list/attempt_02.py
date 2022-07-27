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
        new_head = None

        # define recursive helper function
        def helper(head):
            nonlocal new_head
            # handle base case
            if not head.next:
                new_head = head
                return head
            # handle recursive exploration
            helper(head.next).next = head
            return head
        helper(head)
        head.next = None
        return new_head
