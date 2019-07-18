# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator:

    def __init__(self, root: TreeNode):
        self.stack = list()
        self.pushAll(root)

    def next(self) -> int:
        """
        @return the next smallest number
        """
        ret = self.stack.pop()
        self.pushAll(ret.right)

        return ret.val

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        l = len(self.stack)
        if l:
            return True
        else:
            return False

    def pushAll(self, node):
        while node:
            self.stack.append(node)
            node = node.left

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()