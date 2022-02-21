# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root, target, k: int):
        dist_to_root = 0
        node = root
        while node.val != target.val:
            if node.val < target.val:
                node = node.right
            else:
                node = node.left
            dist_to_root += 1
        # define level order traversal function
        def level(curr, level):
            q = [curr]
            curr_level = -1
            while q:
                next += 1
                curr_level += 1
                if curr_level == level:
                    return [node.val for node in q]
                else:
                    new_q = []
                    for node in q:
                        if node.left is not None:
                            new_q.append(node.left)
                        if node.right is not None:
                            new_q.append(node.right)
                    curr_level += 1
                    q = new_q
            return []
        # call function for distances
        
                
                
