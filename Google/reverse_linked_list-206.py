# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head==None:
            return head
        dummy = ListNode(0)
        dummy.next = head
        start = dummy.next
        cur = start.next
        while cur!=None:
            start.next = cur.next
            cur.next = dummy.next
            dummy.next = cur
            cur = start.next
        return dummy.next