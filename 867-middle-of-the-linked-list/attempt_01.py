from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        tortoise = head
        hair = head
        odd = True
        while hair.next:
            if odd:
                tortoise = tortoise.next
            hair = hair.next
            odd = not odd
        return tortoise
