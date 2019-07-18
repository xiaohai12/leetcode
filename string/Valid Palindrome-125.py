class Solution:
    def isPalindrome(self, s: str) -> bool:
        if s =='':
            return True
        l = len(s)
        s = s.lower()
        left = 0
        right = l-1
        num_l = ord('0')
        num_r= ord('9')
        al_l = ord('a')
        al_r = ord('z')
        while left!=right and right>=0 and left<l:
            l_s = ord(s[left])
            r_s = ord(s[right])
            if l_s>al_r or l_s<num_l or (l_s>num_r and l_s<al_l):
                left+=1
                continue
            if r_s>al_r or r_s<num_l or (r_s>num_r and r_s<al_l):
                right-=1
                continue
            if l_s==r_s:
                left+=1
                right-=1
            else:
                return False
        return True