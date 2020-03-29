class Codec:
    def encode(self, strs: [str]) -> str:
        """Encodes a list of strings to a single string.
        """
        ret = ''
        for s in strs:
            ret += str(len(s)) +'/' +s
        return ret

    def decode(self, s: str) -> [str]:
        """Decodes a single string to a list of strings.
        """
        i = 0
        ret = []
        while i<len(s):
            ind = s[i:].find('/')
            size = int(s[i:i+ind])
            ret.append(s[i+ind+1:i+ind+size+1])
            i += ind + size +1
        return ret


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))