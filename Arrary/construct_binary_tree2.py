# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        l = len(inorder)
        hashmap = {}
        for i in range(l):
            hashmap[inorder[i]] = i
        root = self.helper(inorder, 0, l - 1, postorder, 0, l - 1, hashmap)
        return root

    def helper(self, inorder, inStart, inEnd, postorder, postStart, postEnd, hashmap):
        if inEnd < inStart or postEnd < postStart:
            return None
        r = postorder[postEnd]
        ind = hashmap[r]
        root = TreeNode(r)
        root.left = self.helper(inorder, inStart, ind - 1, postorder, postStart, postStart + ind - inStart - 1, hashmap)
        root.right = self.helper(inorder, ind + 1, inEnd, postorder, postStart + ind - inStart, postEnd - 1, hashmap)
        return root