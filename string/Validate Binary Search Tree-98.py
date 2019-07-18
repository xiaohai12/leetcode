# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return self.isValid(root, -10000000000000, 100000000000000)

    def isValid(self, root, Min, Max):
        if (root == None): return True
        if (root.val >= Max or root.val <= Min): return False
        return self.isValid(root.left, Min, root.val) and self.isValid(root.right, root.val, Max);