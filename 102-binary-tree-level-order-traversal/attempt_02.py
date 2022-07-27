from collections import deque


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def levelOrder(self, root):
        q = deque()
        if root:
            q.appendleft(root)
        q.appendleft(None)
        res = []
        while q:
            batch = []
            curr = q.pop()
            while curr:
                batch.append(curr.val)
                if curr.left:
                    q.appendleft(curr.left)
                if curr.right:
                    q.appendleft(curr.right)
                curr = q.pop()
            if q:
                q.appendleft(None)
            if batch:
                res.append(batch)
        return res
