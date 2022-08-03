from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        even_head = ListNode()
        even_ptr = even_head
        odd_ptr = head
        active = True
        while active:
            # point even list to next even elt
            even_ptr.next = odd_ptr.next
            even_ptr = even_ptr.next
            # point odd element to next odd element
            if not odd_ptr.next or not odd_ptr.next.next:
                active = False
            else:
                odd_ptr.next = odd_ptr.next.next
                odd_ptr = odd_ptr.next
        # point last even node to null
        if even_ptr:
            even_ptr.next = None
        # point last odd element to even list
        odd_ptr.next = even_head.next
        return head
