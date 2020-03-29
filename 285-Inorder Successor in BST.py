# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        if not root:
            return None

        tmp = None
        while root.val != p.val:
            if root.val > p.val:
                tmp = root
                root = root.left
            else:
                root = root.right

        root = root.right
        if not root:
            return tmp

        while root.left:
            root = root.left

        return root