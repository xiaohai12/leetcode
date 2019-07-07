# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if root==None:
            return []
        left = self.postorderTraversal(root.left)
        mid = self.postorderTraversal(root.right)
        return left + mid + [root.val]