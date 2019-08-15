"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""
class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        '''
        ## linear space
        if not head:
            return head 
        cur = head 
        Map = dict()
        while cur:
            clone_node = Node(cur.val,None,None)
            Map[cur] = clone_node
            cur = cur.next 
        cur = head
        while cur:
            next_node = cur.next
            rand = cur.random
            try:
                Map[cur].next = Map[next_node]
            except:
                Map[cur].next = None
            try:
                Map[cur].random = Map[rand]
            except:
                Map[cur].random = None
            cur = cur.next
        return Map[head]
        
        '''

        ## constant space
        if not head:
            return head
        cur = head
        while cur:
            clone_code = Node(cur.val,None,None)
            next_cur = cur.next
            cur.next = clone_code
            clone_code.next = next_cur
            cur = next_cur
        cur = head
        while cur:
            try:
                cur.next.random = cur.random.next
            except:
                cur.next.random = None
            cur = cur.next.next
        cur = head
        tmp_head = Node(0,None,None)
        tmp = tmp_head
        while cur:
            clone = cur.next
            cur.next = clone.next
            tmp.next = clone
            tmp = clone
            cur = cur.next
        return tmp_head.next









