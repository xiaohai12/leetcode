# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        start = ListNode(-1000000000000)
        start.next = head
        slow = start
        fast = start
        while fast.next!=None:
            if fast.val==fast.next.val:
                fast= fast.next
            else:
                slow.next = fast.next
                slow = slow.next
                fast = fast.next
        slow.next = None
        return start.next