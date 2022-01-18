# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root) -> int:
        # utilize bfs with counter
        s = [root]
        if not root:
            s = []
        count = 0
        # outer loop to see if new depth has nodes
        while len(s) > 0:
            new_s = []
            # inner loop pops each node from depth and adds children
            while len(s) > 0:
                curr = s.pop()
                if curr.left:
                    new_s.append(curr.left)
                if curr.right:
                    new_s.append(curr.right)
            # increment count for each level and set new depth
            count += 1
            s = new_s
        return count