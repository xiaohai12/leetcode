# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head == None:
            return False
        tail = head
        ceil = head
        while tail.next != None and tail.next.next != None:
            ceil = ceil.next
            tail = tail.next
            tail = tail.next
            if tail == ceil:
                return True
        return False
