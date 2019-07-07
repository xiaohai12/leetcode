class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if root == None:
            return []
        ret = []
        nodes = [root]
        direction=1
        while nodes:
            ret.append([node.val for node in nodes][::direction])
            nodesPairs = [(node.left, node.right) for node in nodes]
            nodes = [leaf for node in nodesPairs for leaf in node if leaf != None]
            direction *=-1
        return ret