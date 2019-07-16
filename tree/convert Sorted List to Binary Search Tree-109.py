# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if head == None:
            return None
        return self.toBST(head, None)

    def toBST(self, head, tail):
        low = head
        fast = head
        if head == tail:
            return None
        while fast != tail and fast.next != tail:
            low = low.next
            fast = fast.next
            fast = fast.next
        root = TreeNode(low.val)
        root.left = self.toBST(head, low)
        root.right = self.toBST(low.next, tail)
        return root