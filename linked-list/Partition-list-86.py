# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        left = ListNode(0)
        right = ListNode(0)
        pre = left
        post = right

        while head != None:
            if head.val < x:
                pre.next = head
                pre = pre.next
            else:
                post.next = head
                post = post.next
            head = head.next

        post.next = None
        pre.next = right.next
        return left.next

