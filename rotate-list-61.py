# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head
        tmp = head
        L = 0

        # compute the length and mod ind
        while tmp != None:
            L += 1
            tmp = tmp.next
        right = head
        k = k % L

        # compute right part
        ind = 1
        while ind < L - k:
            ind += 1
            right = right.next
        left = right.next
        right.next = None  # setting the next node of right part is None

        res = left
        if left == None:
            return head
        else:
            while left.next != None:
                left = left.next
            left.next = head  # seting the end of left park is the start of right part
        return res
