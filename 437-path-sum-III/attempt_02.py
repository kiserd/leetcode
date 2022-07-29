# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root, targetSum: int):
        # prev attempt passed prefix_sum map, try with global
        prefix_sums = {}

        # define recursive helper function
        def helper(node, curr):
            # handle base case
            if not node:
                return 0
            # handle recursive exploration
            prefix_sums[curr] = prefix_sums.get(curr, 0) + 1
            curr += node.val
            res = prefix_sums.get(curr - targetSum, 0)
            res += helper(node.left, curr)
            res += helper(node.right, curr)
            prefix_sums[curr - node.val] -= 1
            return res
        # kick off helper function
        
        return helper(root, 0)

