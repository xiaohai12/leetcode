# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if len(nums) == 1:
            return TreeNode(nums[0])
        if len(nums) == 0:
            return None

        l = len(nums)
        mid = int(l / 2)
        left = nums[:mid]
        right = nums[mid + 1:]
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(left)
        root.right = self.sortedArrayToBST(right)
        return root
