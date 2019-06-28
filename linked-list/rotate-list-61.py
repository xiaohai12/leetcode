# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head==None or k==0:
            return head
        start = ListNode(0)
        start.next = head
        fast = start
        slow = start
        n = 0
        while fast.next !=None:
            fast = fast.next
            n +=1
        fast = start
        if k%n==0:
            return head         
        for i in range(k%n):
            fast = fast.next
        while fast.next!=None:
            fast = fast.next
            slow = slow.next
        start.next = slow.next
        slow.next = None
        fast.next = head
        return start.next