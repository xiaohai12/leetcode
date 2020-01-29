class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        ret = []
        opened = 0
        for s in S:
            if s=='(' and opened>0:
                ret.append(s)
            if s==')' and opened>1:
                ret.append(s)
            if s=='(':
                opened +=1
            else:
                opened -=1
        return ''.join(ret)

if __name__ == '__main__':
    test = Solution()
    print(test.removeOuterParentheses("((()())(()()))"))