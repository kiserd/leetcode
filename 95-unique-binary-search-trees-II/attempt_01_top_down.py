# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def generateTrees(self, n: int):
        # define recursive function
        def dp(left, right):
            # handle base case
            if right < left:
                return [None]
            # handle recursive case
            if not memo.get((left, right), False):
                memo[(left, right)] = []
                # loop through potential 'next' subtree parents
                for val in range(left, right + 1):
                    # loop through potential 'next' left subtree parents
                    for left_tree in dp(left, val - 1):
                        # loop through potential 'next' right subtree parents
                        for right_tree in dp(val + 1, right):
                            memo[(left, right)].append(TreeNode(val, left_tree, right_tree))
            return memo[(left, right)]
        # build memo and call function
        memo = {}
        return dp(1, n)
