class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:
        stack = []
        low = float('-inf')
        for p in preorder:
            if p < low:
                return False
            while stack and p > stack[-1]:  ## there is a right subtree
                low = stack.pop()  ## pop until pop out the parent of the right subtree
            stack.append(p)
        return True



