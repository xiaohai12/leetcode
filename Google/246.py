class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        dic = {'1':'1','6':'9','8':'8','9':'6','0':'0'}
        for i,s in enumerate(num):
            if s in dic.keys():
                if dic[s]!=num[len(num)-i-1]:
                    return False
            else:
                return False
        return True