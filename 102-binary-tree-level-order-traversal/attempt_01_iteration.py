from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root):
        # attempt to return early on edge case
        if not root:
            return None
        # process using queue
        q = deque()
        q.append(root)
        res = []
        while q:
            level_res = []
            for _ in range(len(q)):
                curr = q.popleft()
                if curr:
                    level_res.append(curr.val)
                # add children to queue for next level
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            res.append(level_res)
        return res
