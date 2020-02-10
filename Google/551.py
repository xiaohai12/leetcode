class Solution:
    def checkRecord(self, s: str) -> bool:
        a = 0
        l = 0
        flag = False
        if 'LLL' in s:
            return False
        for i in s:
            if i == 'A':
                a += 1
                if a > 1:
                    return False

        return True
