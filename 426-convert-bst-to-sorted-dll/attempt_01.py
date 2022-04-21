# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def treeToDoublyList(self, root):
        # handle edge case
        if not root:
            return None
        # define recursive function
        def helper(node):
            # handle base case
            if not node:
                return None, None
            # handle recursive case
            lh, lt = helper(node.left)
            rh, rt = helper(node.right)
            if lt:
                lt.right, node.left = node, lt
            if rh:
                rh.left, node.right = node, rh
            if lh and rt:
                return lh, rt
            if lh:
                return lh, node
            if rt:
                return node, rt
            else:
                return node, node
        h, t = helper(root)
        h.left, t.right = t, h
        return h
