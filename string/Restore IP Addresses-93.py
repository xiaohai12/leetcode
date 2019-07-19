class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        l = len(s)
        if l > 12 or l < 4:
            return []
        self.restoreIp(s, res, 0, '', 0)
        return res

    def restoreIp(self, ipstring, res, ind, restored, count):
        if count == 4 and ind == len(ipstring):
            res.append(restored[:-1])
            return
        for i in range(1, 4):
            if ind + i > len(ipstring):
                break
            s = ipstring[ind:ind + i]
            if i >= 2 and s[0] == '0':
                continue
            if int(s) > 255:
                continue
            self.restoreIp(ipstring, res, ind + i, restored + s + '.', count + 1)


