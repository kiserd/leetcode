# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p, q) -> bool:
        # process trees using stack
        s = [(p, q)]
        while s:
            n1, n2 = s.pop()
            # check for NoneType w/ XOR
            if n1 and not n2 or not n1 and n2:
                return False
            # handle case where nodes are NOT NoneType
            if n1:
                # check for unequal vals
                if n1.val != n2.val:
                    return False
                # append children to stack
                s.append((n1.left, n2.left))
                s.append((n1.right, n2.right))
        # all tests passed, indicate True to calling function
        return True
