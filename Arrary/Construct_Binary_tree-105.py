# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        in_len = len(inorder)
        hashmap = {}
        for i in range(in_len):
            hashmap[inorder[i]] = i
        root = self.helper(preorder, 0, inorder, 0, in_len - 1, hashmap)
        return root

    def helper(self, preorder, prestart, inorder, inStart, inEnd, hashmap):
        if prestart > len(preorder) - 1 or inStart > inEnd:
            return None
        root = TreeNode(preorder[prestart])
        ind = hashmap[preorder[prestart]]
        root.left = self.helper(preorder, prestart + 1, inorder, inStart, ind - 1, hashmap)
        root.right = self.helper(preorder, prestart + 1 + ind - inStart, inorder, ind + 1, inEnd, hashmap)
        return root