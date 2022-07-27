# one major hangup in my attempts to implement solution from intuition/memory:
### recursion will always explore the left-more subtree first. Hence, one is
### safe using the global idx to process preorder by simply incrementing the
### global idx each recursive dive.

# I had attempted to get tricky with passing something like
### 2 * idx + 1 to the left subtree, but this doesn't work when preorder does
### not acknowledge nulls


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder, inorder):
        # build value to index mapping for inorder
        val_to_idx = {}
        for idx, val in enumerate(inorder):
            val_to_idx[val] = idx
        # define recursive helper function
        def helper(lt, rt):
            nonlocal idx
            # handle base case
            if rt < lt:
                return None
            # handle recursive exploration
            val = preorder[idx]
            root = TreeNode(val)
            idx += 1
            root.left = helper(lt, val_to_idx[val] - 1)
            root.right = helper(val_to_idx[val] + 1, rt)
            return root
        idx = 0
        return helper(0, len(inorder) - 1)

