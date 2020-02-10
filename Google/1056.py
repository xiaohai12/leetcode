class Solution:
    def confusingNumber(self, N: int) -> bool:
        dic = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}
        str_N = str(N)
        ret = ''
        for i in range(len(str_N) - 1, -1, -1):
            if str_N[i] not in dic.keys():
                return False
            ret += dic[str_N[i]]
        if ret == str_N:
            return False
        return True
