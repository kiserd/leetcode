# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root, p):
        arr = self.inorderList(root)
        for i in range(len(arr)):
            if i < len(arr) - 1 and p == arr[i]:
                return arr[i + 1]
        return None

    def inorderList(self, root):
        # handle base case
        if not root:
            return []
        # recursively explore subtrees
        left_sub = self.inorderList(root.left)
        right_sub = self.inorderList(root.right)
        return left_sub + [root] + right_sub