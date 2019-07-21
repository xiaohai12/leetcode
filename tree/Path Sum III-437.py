# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        if not root:
            return 0
        presum = dict()
        presum[0] = 1
        return self.helper(root, presum, 0, sum)

    def helper(self, root, presum, cursum, target):
        if not root:
            return 0
        cursum += root.val
        res = presum.get(cursum - target, 0)
        presum[cursum] = presum.get(cursum, 0) + 1
        res += self.helper(root.left, presum, cursum, target) + self.helper(root.right, presum, cursum, target)
        presum[cursum] = presum[cursum] - 1
        return res