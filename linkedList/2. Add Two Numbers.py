# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        s = 0
        dump = ListNode(0)
        ret = dump
        while l1 != None or l2 != None:  ## or is better than and !
            s = int(s / 10)
            if l1:
                s += l1.val
                l1 = l1.next
            if l2:
                s += l2.val
                l2 = l2.next

            dump.next = ListNode(s % 10)
            dump = dump.next

        if s > 9:
            dump.next = ListNode(1)

        return ret.next

