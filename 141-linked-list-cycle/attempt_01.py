from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        tortoise = head
        hair = head
        odd = False
        while hair:
            if odd:
                tortoise = tortoise.next
            hair = hair.next
            odd = not odd
            if tortoise == hair:
                return True
        return False
