# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA, headB):
        # get lengths of LLs
        count_a = 1
        count_b = 1
        a_ptr = headA
        b_ptr = headB
        while a_ptr.next:
            count_a += 1
            a_ptr = a_ptr.next
        while b_ptr.next is not None:
            count_b += 1
            b_ptr = b_ptr.next
        # iterate longer of LLs until remaining nodes is equal
        a_ptr = headA
        b_ptr = headB
        if count_a < count_b:
            count_a, count_b = count_b, count_a
            a_ptr, b_ptr = b_ptr, a_ptr
        for _ in range(count_a - count_b):
            a_ptr = a_ptr.next
        # iterate LLs at same time to find intersecting node
        while a_ptr != b_ptr:
            a_ptr = a_ptr.next
            b_ptr = b_ptr.next
        return a_ptr
