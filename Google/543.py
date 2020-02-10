# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.ans = 0
        if root == None:
            return 0
        deep = self.deep(root)

        return self.ans

    def deep(self, root):

        if root == None:
            return 0
        left = self.deep(root.left)
        right = self.deep(root.right)
        a = max(left, right)
        self.ans = max(self.ans, left + right)
        return 1 + a