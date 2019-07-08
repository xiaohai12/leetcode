# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        if not root:
            return 0
        lists = []
        cur = 0
        self.backtrack(root, lists, cur)
        return sum(lists)

    def backtrack(self, root, lists, cur):
        if not root.left and not root.right:
            cur = cur * 10 + root.val
            lists.append(cur)
        cur = cur * 10 + root.val
        if root.left:
            self.backtrack(root.left, lists, cur)

        if root.right:
            self.backtrack(root.right, lists, cur)
