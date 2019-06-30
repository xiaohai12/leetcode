# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        # if head==None:
        #     return head
        # head.next = self.removeElements(head.next,val)
        # if head.val==val:
        #     head = head.next
        # return head

        dummy = ListNode(0)
        dummy.next = head
        cur = head
        pre = dummy
        while cur != None:
            if cur.val == val:
                pre.next = cur.next
            else:
                pre = pre.next
            cur = cur.next
        return dummy.next 