from typing import List


"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    def preorder(self, root) -> List[int]:
        # define recursive helper function
        def helper(node):
            # handle base case
            if not node:
                return []
            # handle recursive exploration
            res = [node.val]
            for child in node.children:
                res += helper(child)
            return res
        return helper(root)
