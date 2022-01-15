# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head):
        if head is None:
            return None
        even = False
        odds = head
        even_head = ListNode()
        evens = even_head
        prev = odds
        while odds is not None:
            # print('odds: ', odds)
            # print('evens: ', evens)
            # print('even: ', even)
            if even:
                evens.next = odds
                odds = odds.next
                prev.next = odds
                evens = evens.next
                evens.next = None
                even = not even
            else:
                prev = odds
                odds = odds.next
                even = not even
        # append evens to end of odds
        prev.next = even_head.next
        return head

# seems that attacking this from the even side of things would be a bit
# cleaner
            
