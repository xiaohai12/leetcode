# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root == None:
            return []
        ret = []
        nodes = [root]
        while nodes:
            ret.append([node.val for node in nodes])
            nodesPairs = [(node.left, node.right) for node in nodes]
            nodes = [leaf for node in nodesPairs for leaf in node if leaf != None]
        return ret
