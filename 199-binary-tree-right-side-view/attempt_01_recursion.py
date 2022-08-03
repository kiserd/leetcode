from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # define recursive helper function
        def helper(node):
            # handle base case
            if not node:
                return []
            # handle recursive exploration
            left = helper(node.left)
            right = helper(node.right)
            res = right
            # handle case where left subtree is longer than right
            if len(left) > len(right):
                for idx in range(len(right), len(left)):
                    res.append(left[idx])
            return [node.val] + res
        return helper(root)
