# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root):
        # init helper data struct
        encountered = {}
        res = set()
        # define recursive exploratory function
        def rec(node):
            # handle base case
            if not node:
                return (None, )
            # handle recursive exploration
            subtree = (node.val, ) + rec(node.left) + rec(node.right)
            if subtree in encountered:
                if encountered[subtree]:
                    res.add(node)
                    encountered[subtree] = False
            else:
                encountered[subtree] = True
            return subtree
        rec(root)
        return res
