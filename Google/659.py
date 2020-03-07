class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        freq = {}
        appendfreq = {}
        for num in nums:
            freq[num] =  freq.get(num,0)+1
        for num in nums:
            if freq.get(num,0)==0:
                continue
            elif appendfreq.get(num,0)>0:
                appendfreq[num] = appendfreq[num] -1
                appendfreq[num+1] = appendfreq.get(num+1,0)+1
            elif freq.get(num+1,0)!=0 and freq.get(num+2,0)!=0:
                freq[num+1] -=1
                freq[num+2] -=1
                appendfreq[num+3] = appendfreq.get(num+3,0)+1
            else:
                return False
            freq[num] -=1
        return True