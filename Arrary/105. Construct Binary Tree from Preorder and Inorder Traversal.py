# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if preorder == []:
            return None
        root = preorder[0]
        Node = TreeNode(root)
        ind = inorder.index(root)
        Node.left = self.buildTree(preorder[1:ind + 1], inorder[:ind])
        Node.right = self.buildTree(preorder[ind + 1:], inorder[ind + 1:])
        return Node

