# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head, k: int):
        # handle empty LL
        if not head: return head
        # get length of LL
        size = 1
        orig_tail = head
        while orig_tail.next:
            orig_tail = orig_tail.next
            size += 1
        # simplify size
        k %= size
        # attempt to return early
        if not k:
            return head
        # get new tail
        count = 1
        new_tail = head
        while count < size - k:
            new_tail = new_tail.next
            count += 1
        new_head = new_tail.next
        # build new LL
        orig_tail.next = head
        new_tail.next = None
        return new_head