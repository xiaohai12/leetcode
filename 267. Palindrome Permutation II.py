class Solution:
    def generatePalindromes(self, s: str) -> List[str]:
        if len(s) == 1:
            return [s]
        elif len(s) == 0:
            return []

        rec = {}
        odd = 0
        stack = []
        for i in s:
            rec[i] = rec.get(i, 0) + 1
            if rec[i] % 2 == 1:
                odd += 1
            else:
                odd -= 1
        if odd > 1:
            return []
        mid = ''
        for key in rec.keys():
            val = rec[key]
            if val % 2 == 1:
                mid = key
            for i in range(int(val / 2)):
                stack.append(key)

        flag = [False] * len(stack)
        tmp = ''
        ret = []
        self.helper(tmp, stack, flag, mid, ret)
        return ret

    def helper(self, tmp, stack, flag, mid, ret):
        if len(tmp) == len(stack):
            ret.append(tmp + mid + tmp[::-1])
            return

        for i in range(len(stack)):
            ### aovid duplication ??????
            if i > 0 and stack[i] == stack[i - 1] and not flag[i - 1]:
                continue

            if flag[i] == False:
                tmp += stack[i]
                flag[i] = True
                self.helper(tmp, stack, flag, mid, ret)
                flag[i] = False
                tmp = tmp[:-1]
