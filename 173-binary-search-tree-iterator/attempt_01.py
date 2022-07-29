from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = [(root, False)]

    def next(self) -> int:
        curr, is_val = self.stack.pop()
        while not is_val:
            if curr.right:
                self.stack.append((curr.right, False))
            self.stack.append((curr.val, True))
            if curr.left:
                self.stack.append((curr.left, False))
            curr, is_val = self.stack.pop()
        return curr

    def hasNext(self) -> bool:
        return len(self.stack) > 0


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
