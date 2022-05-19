# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root, target: float) -> int:
        # define recursive helper
        def search(node):
            # handle base case
            if not node:
                return None
            # handle recursive exploration
            future = None
            if target < node.val:
                future = search(node.left)
            else:
                future = search(node.right)
            if future is None:
                return node.val
            elif abs(future - target) < abs(node.val - target):
                return future
            else:
                return node.val
        return search(root)
