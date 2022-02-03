"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root):
        # handle edge case
        if root is None: return None
        q = [root]
        next = 0
        res = []
        while next < len(q):
            batch = []
            for _ in range(len(q) - next):
                curr = q[next]
                batch.append(curr.val)
                q += curr.children
                next += 1
            res.append(batch)
        return res
