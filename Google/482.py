class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        S = S.replace('-', '')
        S = S.upper()
        start = len(S) % K
        if start == 0:
            start = K
        ret = ''
        for i in range(len(S)):
            ret += S[i]
            if i % K == start - 1 and i != len(S) - 1:
                ret += '-'

        return ret

