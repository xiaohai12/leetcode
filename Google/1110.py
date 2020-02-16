# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    ## hua hua jiang shi pin
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        ans = []
        to_delete = set(to_delete)

        def process(n):
            if not n:
                return n
            n.left, n.right = process(n.left), process(n.right)
            if n.val not in to_delete:
                return n
            if n.left:
                ans.append(n.left)
            if n.right:
                ans.append(n.right)
            return None

        root = process(root)
        if root:
            ans.append(root)
        return ans
