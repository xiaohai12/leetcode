# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if root == None:
            return True
        return self.DFShight(root) != -1

    def DFShight(self, root):
        if root == None:
            return 0
        leftHight = self.DFShight(root.left)
        if leftHight == -1: return -1
        rightHight = self.DFShight(root.right)
        if rightHight == -1: return -1

        if abs(leftHight - rightHight) > 1: return -1

        return max(leftHight, rightHight) + 1

