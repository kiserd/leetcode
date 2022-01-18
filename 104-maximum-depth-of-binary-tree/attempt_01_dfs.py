# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root) -> int:
        # utilize stack in dfs
        s = [(root, 1)]
        max_depth = 0
        while len(s) > 0:
            curr, depth = s.pop()
            max_depth = max(max_depth, depth)
            if curr.left:
                s.append((curr.left, depth + 1))
            if curr.right:
                s.append((curr.right, depth + 1))
        return max_depth