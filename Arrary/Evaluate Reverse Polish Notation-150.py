class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        if len(tokens) == 1:
            return tokens[0]
        tmp = []
        signal = ['+', '-', '*', '/']
        for item in tokens:
            if item not in signal:
                tmp.append(item)
            else:
                sig = item
                num2 = tmp.pop()
                num1 = tmp.pop()
                num3 = self.operation(num1, num2, sig)
                print(num3)
                tmp.append(num3)
        return tmp[-1]

    def operation(self, num1, num2, sig):
        if sig == '+':
            return int(num1) + int(num2)
        elif sig == '-':
            return int(num1) - int(num2)
        elif sig == '*':
            return int(num1) * int(num2)
        elif sig == '/':
            div = int(num1) / int(num2)
            return int(div) 