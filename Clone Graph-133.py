"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
"""


class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if node == None:
            return None
        queue = [node]
        Map = {node: Node(node.val, [])}
        while queue:
            n = queue.pop()
            for neighbor in n.neighbors:
                if neighbor not in Map.keys():
                    new = Node(neighbor.val, [])
                    Map[neighbor] = new
                    queue = [neighbor] + queue
                    Map[n].neighbors.append(new)
                else:
                    Map[n].neighbors.append(Map[neighbor])
        return Map.get(node)

