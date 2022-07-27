# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root, targetSum: int):
        # handle edge case
        if not root:
            return []
        # define recursive helper function
        def helper(node, target):
            # handle base case where we hit empty node from non-leaf
            if not node:
                return []
            # decrement target by node val
            target -= node.val
            # handle base case(s)
            if not node.left and not node.right:
                if target == 0:
                    return [[node.val]]
                else:
                    return []
            # handle recursive exploration
            res = []
            for path in helper(node.left, target):
                res.append([node.val] + path)
            for path in helper(node.right, target):
                res.append([node.val] + path)
            return res
        # kick off helper function
        return helper(root, targetSum)
