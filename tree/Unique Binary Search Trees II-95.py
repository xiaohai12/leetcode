# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        if n == 0:
            return []
        return self.genTrees(1, n)

    def genTrees(self, start, end):
        ret = []

        if end < start:
            return [None]
        if end == start:
            return [TreeNode(start)]
        for i in range(start, end + 1):
            left = self.genTrees(start, i - 1)
            right = self.genTrees(i + 1, end)

            for sub_l in left:
                for sub_r in right:
                    root = TreeNode(i)
                    root.left = sub_l
                    root.right = sub_r
                    ret.append(root)
        return ret
