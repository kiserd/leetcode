# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head):
        if head is None:
            return None
        odds = head
        even_head = odds.next
        evens = even_head
        while evens is not None:
            print('odds: ', odds)
            print('evens: ', evens)
            odds.next = evens.next
            odds = odds.next
            evens.next = odds.next
        # append evens to end of odds
        # prev.next = even_head.next
        return head

# making second attempt at this problem, but using evens as the while-loop
# driver
            
