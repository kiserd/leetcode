# I was on the right path with this one, but was getting stuck in executing
# the details. I knew to create the global variable to keep track of the max
# "subtree" (what I was calling it), while continuing to recursively search for
# a better solution.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root) -> int:
        # define recursive helper function
        def helper(node):
            nonlocal glob
            # handle base case
            if not node:
                return 0
            # handle recursive exploration
            left = max(helper(node.left), 0)
            right = max(helper(node.right), 0)
            # here we only update global variable if we found a new optimal
            # "root" or greatest ancestor node
            glob = max(glob, left + right + node.val)
            # this provides the value we need to continue our recursive search
            return max(left, right, 0) + node.val
        # use global max as dumb little hack
        glob = -1001
        # kick off helper function
        helper(root)
        return glob
        
