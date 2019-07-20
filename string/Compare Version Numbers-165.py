class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        ver1 = version1.split('.')
        ver2 = version2.split('.')
        l1 = len(ver1)
        l2 = len(ver2)
        s1 = 0
        s2 = 0
        l = max(l1,l2)
        for i in range(l):
            if i<l1:
                v1  = int(ver1[i])
            else:
                v1 = 0
            if i<l2:
                v2 = int(ver2[i])
            else:
                v2 = 0
            s1 +=v1 *10**(-i)
            s2 +=v2 *10**(-i)
        if s1<s2:
            return -1
        elif s1>s2:
            return 1
        else:
            return 0