# definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums):
        # define recursive helper function
        def build(lo, hi):
            # handle base cases
            if hi < lo:
                return None
            # handle recursive exploration/processing
            mid = lo + (hi - lo) // 2
            return TreeNode(nums[mid], build(lo, mid - 1), build(mid + 1, hi))
        # kick off function and return result to calling function
        return build(0, len(nums) - 1)
