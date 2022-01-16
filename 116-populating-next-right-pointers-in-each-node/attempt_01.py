"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root):
        # start with the leftmost node at the level
        root.next = None
        start = root
        # outer loop until our start is not null
        while start is not None:
            # inner loop continues until we have no right-next
            curr = start
            while curr is not None:
                # set left child's next
                curr.left.next = curr.right
                # set right child's next
                if curr.next is None:
                    curr.right.next is None
                else:
                    curr.right.next = curr.next.left
                # iterate to next sibling/cousin
                curr = curr.next
            # move on to our current start's left child
            start = start.left
        return root


# feels like we should be using a queue with some sort of delimiter, but that
# would require O((n + 1) / 2) = O(n) space

# we need to walk through the tree in a BFS manner