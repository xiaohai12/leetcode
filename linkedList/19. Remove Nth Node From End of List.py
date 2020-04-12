# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if not head:
            return None

        dummy = ListNode(0)
        dummy.next = head
        faster = dummy  ## start from dummy is better !
        lower = dummy

        while n >= 0 and faster != None:
            faster = faster.next
            n -= 1

        while faster != None:
            faster = faster.next
            lower = lower.next

        if lower.next == None:
            return dummy

        lower.next = lower.next.next

        return dummy.next

