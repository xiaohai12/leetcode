# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def longestConsecutive(self, root: TreeNode) -> int:
        if not root:
            return 0

        self.max = 0
        self.helper(root, 0, root.val)
        return self.max

    def helper(self, root, cur, val):
        if not root:
            return
        if root.val == val:
            cur += 1
        else:
            cur = 1
        self.max = max(self.max, cur)
        self.helper(root.left, cur, root.val + 1)
        self.helper(root.right, cur, root.val + 1)