# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head==None or head.next==None:
            return None
        low = head
        fast = head
        start = head
        while low!=None and fast!=None:
            fast = fast.next
            if fast==None:
                return None
            fast = fast.next
            low = low.next
            if fast==low:
                while start!=fast:
                    fast = fast.next
                    start = start.next
                return start
        return None 