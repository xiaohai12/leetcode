class Solution:
    def toLowerCase(self, str: str) -> str:
        up = ord('Z')
        low = ord('A')
        ret = ''
        for s in str:
            code = ord(s)
            if code <= up and code >= low:
                ret += chr(ord(s) + 32)
            else:
                ret += s
        return ret

