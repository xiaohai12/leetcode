# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        start = ListNode(0)
        tmp = start
        while l1 != None and l2 != None:
            if l1.val < l2.val:
                start.next = l1
                l1 = l1.next
            else:
                start.next = l2
                # l1 = l1.next
                l2 = l2.next
            start = start.next
        if l1 == None:
            start.next = l2
        else:
            start.next = l1
        return tmp.next
