# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:
        if root == None:
            return None
        left = self.depth(root.left)
        right = self.depth(root.right)
        if left == right:
            return root
        if left > right:
            return self.lcaDeepestLeaves(root.left)
        else:
            return self.lcaDeepestLeaves(root.right)

    def depth(self, root):
        if root == None:
            return 0
        if root.left == None and root.right == None:
            return 1
        return 1 + max(self.depth(root.left), self.depth(root.right))
