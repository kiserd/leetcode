from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # count the nodes
        n = 1
        curr = head
        while curr.next:
            n += 1
            curr = curr.next
        # use stack to determine palindrome property
        stack = []
        even = n % 2 == 0
        ct = 1
        curr = head
        while ct <= n // 2:
            stack.append(curr.val)
            curr = curr.next
            ct += 1
        if not even:
            curr = curr.next
        while curr:
            elt = stack.pop()
            if curr.val != elt:
                return False
            curr = curr.next
        return True
