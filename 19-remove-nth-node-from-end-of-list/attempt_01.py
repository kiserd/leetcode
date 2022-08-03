from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head, n: int) -> Optional[ListNode]:
        # init pointers
        tortoise = head
        hair = head
        # progress hair to (n+1)th node
        count = 0
        while count < n:
            hair = hair.next
            count += 1
        # progress tortoise and hair until hair hits null
        while hair and hair.next:
            hair = hair.next
            tortoise = tortoise.next
        # handle edge case: n == sz
        if not hair:
            return head.next
        tortoise.next = tortoise.next.next
        return head
