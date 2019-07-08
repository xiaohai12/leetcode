# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if not root:
            return []
        lists = []
        tmp = [root.val]
        self.backtrack(root, sum - root.val, lists, tmp)
        return lists

    def backtrack(self, root, sum, lists, tmp):
        if sum == 0 and not root.left and not root.right:
            lists.append(tmp.copy())

        if root.right:
            sum -= root.right.val
            tmp.append(root.right.val)
            self.backtrack(root.right, sum, lists, tmp)
            sum += root.right.val
            tmp.pop()

        if root.left:
            sum -= root.left.val
            tmp.append(root.left.val)
            self.backtrack(root.left, sum, lists, tmp)
            sum += root.left.val
            tmp.pop()
 