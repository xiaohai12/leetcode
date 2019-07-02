# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        if head == None or head.next == None:
            return head

        dummy = ListNode(0)
        dummy.next = head
        slow = dummy
        fast = dummy
        while fast.next != None and fast.next.next != None:
            fast = fast.next
            fast = fast.next
            slow = slow.next
            # reverse the right half of linked list
        start = slow.next
        cur = start.next
        while cur != None:
            start.next = cur.next
            cur.next = slow.next
            slow.next = cur
            cur = start.next

        left = head
        right = slow.next
        while left != slow:
            slow.next = right.next
            right.next = left.next
            left.next = right
            left = right.next
            right = slow.next
        return dummy.next 