# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def zigzagLevelOrder(self, root):
        # handle edge case
        if not root: return []
        # use bfs with deque
        dq = deque()
        dq.append(root)
        res = []
        dir = True
        # while depth still has nodes
        while dq:
            curr = []
            new_dq = deque()
            while dq:
                # get next node in queue and process
                node = dq.popleft()
                curr.append(node.val)
                if node.left: new_dq.append(node.left)
                if node.right: new_dq.append(node.right)
            # reverse current depth every other depth
            if not dir:
                curr.reverse()
            res.append(curr)
            # iterate variables for next depth
            dq = new_dq
            dir = not dir
        return res
