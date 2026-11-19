class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or len(s) < len(t):
            return ""
        
        tMap = {}
        for ch in t:
            tMap[ch] = tMap.get(ch, 0) + 1

        required = len(tMap)
        window = {}
        formed, l = 0, 0
        best_len, best_l = float("inf"), 0

        for r in range(len(s)):
            window[s[r]] = window.get(s[r], 0) + 1
            if (s[r] in tMap and window[s[r]] == tMap[s[r]]):
                formed += 1

            while formed == required:
                if r - l + 1 < best_len:
                    best_len = r - l + 1
                    best_l = l
                    
                window[s[l]] -= 1
                if s[l] in tMap and window[s[l]] < tMap[s[l]]:
                    formed -= 1
                l += 1
        return "" if best_len == float("inf") else s[best_l:best_l + best_len]


            

            
             
