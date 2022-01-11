# solution becomes much more simple when not using the helper function in
# attempt_01

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root):
        # handle base case of None
        if root is None:
            return None
        # recursively explore left and right subtree
        root.left = self.pruneTree(root.left)
        root.right = self.pruneTree(root.right)
        # handle case where node needs pruned
        if root.left is None and root.right is None and root.val == 0:
            return None
        # return false indicating that subtree should not be pruned
        return root