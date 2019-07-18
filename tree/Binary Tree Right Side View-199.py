# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        ret=[]
        ret.append(root.val)
        left = self.rightSideView(root.left)
        right = self.rightSideView(root.right)
        l = len(right)
        try:
            rightView = right + left[l:]
        except:
            rightView = right
        return ret+rightView