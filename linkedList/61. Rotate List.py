# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if head == None:
            return head

        dummy = ListNode(0)
        dummy.next = head
        tmp = head
        length = 1
        while tmp.next != None:
            tmp = tmp.next
            length += 1
        k %= length
        if k == 0:
            return head
        right = dummy
        left = dummy
        for i in range(k):
            right = right.next
        while right.next != None:
            left = left.next
            right = right.next
        dummy.next = left.next
        left.next = None
        right.next = head
        return dummy.next






