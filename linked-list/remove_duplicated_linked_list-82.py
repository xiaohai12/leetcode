
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

        if head == None:
            return head
        start = ListNode(0)
        start.next = head
        slow = start
        fast = head
        flag = False
        while fast.next != None:
            if fast.val == fast.next.val:
                fast = fast.next
                flag = True
            elif flag == True:
                fast = fast.next
                flag = False
            else:
                slow.next = fast
                fast = fast.next
                slow = slow.next
        if flag == False:
            slow.next = fast
        else:
            slow.next = None
        return start.next
    '''
    if head==None:
            return head 
        start = ListNode(0)
        start.next = head 
        slow = start
        fast = start 
        while fast!=None:
            while (fast.next!=None and fast.val==fast.next.val):
                fast = fast.next 
            if slow.next==fast:
                slow = slow.next 
            else:
                slow.next = fast.next 
            fast = fast.next 
        return start.next '''
