# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        leftdep = self.leftDep(root.left)
        rightdep = self.rightDep(root.right)
        if leftdep == rightdep:
            return 2 ** (leftdep + 1) - 1
        ## O(n) solution
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)

    def leftDep(self, root):
        if not root:
            return 0
        return 1 + self.leftDep(root.left)

    def rightDep(self, root):

        if not root:
            return 0
        return 1 + self.rightDep(root.right)
