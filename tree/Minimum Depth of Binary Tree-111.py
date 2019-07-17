# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root == None:
            return 0

        if root.left == None and root.right == None:
            return 1
        left = 1000000000
        right = 10000000000
        if root.left:
            left = self.minDepth(root.left)
        if root.right:
            right = self.minDepth(root.right)

        return min(left, right) + 1
