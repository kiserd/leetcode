from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # use global variable as little hack
        count = 0
        glob = None

        # define recursive helper function
        def helper(node):
            nonlocal count
            nonlocal glob
            # handle base case
            if not node:
                return
            # handle recursive exploration
            helper(node.left)
            count += 1
            if count == k:
                glob = node.val
            helper(node.right)
        helper(root)
        return glob
