# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder, inorder):
        def helper(left, right):
            # use nonlocal to refer to next root idx
            nonlocal idx
            # handle base case
            if left > right: return None
            # construct the root node
            root_val = preorder[idx]
            root = TreeNode(root_val)
            idx += 1
            # recursively build left and right subtree
            root_idx = num_to_idx[root_val]
            root.left = helper(left, root_idx - 1)
            root.right = helper(root_idx + 1, right)
            return root
        # create inorder num to idx mapping
        num_to_idx = {}
        for i, num in enumerate(inorder):
            num_to_idx[num] = i
        # initialize global root idx tracker
        idx = 0
        return helper(0, len(preorder) - 1)


# definitely need to return to this down the road and build from memory.
# this first attempt relied HEAVILY on the solution provided by LC.
# going to take a hack at some of the other 'construct tree from...' problems
    