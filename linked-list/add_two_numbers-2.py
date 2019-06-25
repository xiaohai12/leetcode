# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        ret = ListNode(0)
        tmp = ret
        flag = 0
        while l1 != None or l2 != None:
            val = self.value(l1) + self.value(l2) + flag
            if val > 9:
                flag = 1
                val = val % 10
            else:
                flag = 0
            tmp.next = ListNode(val)
            tmp = tmp.next
            l1 = self.Next(l1)
            l2 = self.Next(l2)
        if flag == 1:
            tmp.next = ListNode(1)
            tmp = tmp.next
        return ret.next

    def value(self, l):
        if l != None:
            return l.val
        else:
            return 0

    def Next(self, l):
        if l != None:
            return l.next
        else:
            return l