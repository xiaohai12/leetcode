# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def constructFromPrePost(self, pre: List[int], post: List[int]) -> TreeNode:
        if pre == []:
            return None
        root = TreeNode(pre[0])
        if len(pre) == 1:
            return root
        left_root = pre[1]
        ind = post.index(left_root)
        left_pre = pre[1:ind + 2]
        left_post = post[:ind + 1]

        right_pre = pre[ind + 2:]
        right_post = post[ind + 1:]
        root.left = self.constructFromPrePost(left_pre, left_post)
        root.right = self.constructFromPrePost(right_pre, right_post)
        return root
