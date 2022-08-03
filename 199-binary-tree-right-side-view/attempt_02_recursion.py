from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # handle base case
        if not root:
            return []
        # handle recursive exploration
        left = self.rightSideView(root.left)
        right = self.rightSideView(root.right)
        res = right
        # handle case where left subtree is longer than right
        if len(left) > len(right):
            for idx in range(len(right), len(left)):
                res.append(left[idx])
        return [root.val] + res
