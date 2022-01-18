# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root, k: int) -> int:
        # use inorder traversal with a counter
        count = 1
        stack = [root]
        node = root
        while len(stack) > 0:
            # traverse left descendants to leaf
            while node.left:
                stack.append(node.left)
                node = node.left
            # work back from leftmost leaf
            curr = stack.pop()
            if count == k:
                return curr.val
            count += 1
            if curr.right:
                stack.append(curr.right)
                node = curr.right
        