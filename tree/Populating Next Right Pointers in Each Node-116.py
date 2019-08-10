"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        tmp = root
        while (tmp and tmp.left):
            cur = tmp
            # each layer
            while cur:
                cur.left.next = cur.right
                if cur.next == None:
                    cur.right.next = None
                else:
                    cur.right.next = cur.next.left
                cur = cur.next
            tmp = tmp.left
        return root

