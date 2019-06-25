class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next ==None:
            return head
        n = head.next
        head.next = self.swapPairs(head.next.next)
        n.next = head
        return n 