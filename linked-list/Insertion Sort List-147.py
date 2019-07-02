# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        while head and head.next:
            if head.val>head.next.val:
                insertNode = head.next
                pre = dummy
                while pre.next.val<insertNode.val:
                    pre = pre.next
                head.next = insertNode.next
                insertNode.next = pre.next
                pre.next = insertNode
            else:
                head = head.next
        return dummy.next