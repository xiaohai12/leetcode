# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if postorder==[]:
            return None
        root = postorder[-1]
        ind = inorder.index(root)
        Node = TreeNode(root)
        Node.left = self.buildTree(inorder[:ind],postorder[:ind])
        Node.right = self.buildTree(inorder[ind+1:],postorder[ind:-1])
        return Node 