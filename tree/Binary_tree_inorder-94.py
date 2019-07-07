# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if root ==None:
            return []
        ret = []
        left = self.preorderTraversal(root.left)
        right = self.preorderTraversal(root.right)
        return ret+[root.val]+left+right