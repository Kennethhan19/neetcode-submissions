class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if s1 is None or s2 is None or not s1 or not s2 or len(s1) > len(s2):
            return False

        s1_cnt = [0]*26
        for s in s1:
            pos = ord(s) - ord('a') 
            s1_cnt[pos] += 1
        
        l = 0
        s2_cnt = [0]*26
        for r in range(len(s2)):
            rPos = ord(s2[r]) - ord('a') 
            s2_cnt[rPos] += 1

            while r - l + 1 > len(s1):
                lPos = ord(s2[l]) - ord('a')
                s2_cnt[lPos] -= 1
                l += 1
            
            if s2_cnt == s1_cnt:
                return True
            
        return False