# this was the approach that came to mind immediately, check out the solution
# for several more approaches

# one interesting takeaway is that the appropriate approach depends heavily
# upon the length of lists (n) vs. number of lists (k)

# if the length of the lists are 'shallow', it could make sense to go about
# things merging the lists together one-by-one

import heapq

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists):
        # initialize heap
        h = []
        for i, head in enumerate(lists):
            if head:
                h.append((head.val, i))
                lists[i] = lists[i].next
        heapq.heapify(h)
        # process and replenish heap
        head = ListNode()
        curr = head
        while h:
            val, idx = heapq.heappop(h)
            new_node = ListNode(val)
            curr.next = new_node
            curr = curr.next
            if lists[idx]:
                heapq.heappush(h, (lists[idx].val, idx))
                lists[idx] = lists[idx].next
        if not head.next:
            return None
        return head.next
