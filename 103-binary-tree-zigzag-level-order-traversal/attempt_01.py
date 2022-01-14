# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root):
        pass        




# dumb attempt

# class Solution:
#     def zigzagLevelOrder(self, root):
#         q = [root]
#         next = 0
#         res = []
#         size = 1
#         rev = True
#         while next < len(q):
#             rev = not rev
#             curr = []
#             for _ in range(size):
#                 if next == len(q):
#                     break
#                 node = q[next]
#                 next += 1
#                 curr.append(node.val)
#                 if node.left:
#                     q.append(node.left)
#                 if node.right:
#                     q.append(node.right)
#             if rev:
#                 curr.reverse()
#             res.append(curr)
#             size *= 2
#         return res