# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        '''
        left = ListNode(0)
        reverse = ListNode(0)
        p1 = left
        p2 = reverse
        rev = []
        i = 1
        while i <= n:
            if i < m:
                p1.next = head
                p1 = p1.next
            else:
                rev.append(head.val)
            i += 1
            head = head.next

        for i in range(len(rev) - 1, -1, -1):
            p2.next = ListNode(rev[i])
            p2 = p2.next
        p2.next = head
        p1.next = reverse.next

        return left.next
        
        '''
        #a better one

        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        for i in range(m - 1):
            pre = pre.next
        start = pre.next
        cur = start.next

        for i in range(n - m):
            start.next = cur.next
            cur.next = pre.next
            pre.next = cur
            cur = start.next

        return dummy.next

