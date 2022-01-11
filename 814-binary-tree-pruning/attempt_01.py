# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root):
        self.prune(root)
        if root.val == 0 and root.left is None and root.right is None:
            root = None
        return root
    
    def prune(self, node):
        # handle base case of None
        if node is None:
            return True
        # recursively explore left and right subtree
        left_prune = self.prune(node.left)
        right_prune = self.prune(node.right)
        # handle case where both sides need pruned
        if left_prune and right_prune:
            node.left = None
            node.right = None
            return True and node.val == 0
        # handle case of pruning only one side
        if left_prune:
            node.left = None
        elif right_prune:
            node.right = None
        # return false indicating that subtree should not be pruned
        return False