class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # time: O(N)
        # space: O(1)
        if not t or len(s) < len(t):
            return ""
        
        tMap = {}
        for ch in t:
            tMap[ch] = tMap.get(ch, 0) + 1

        required = len(tMap) # distinct chars that must be satisfied
        window = {}
        formed, l = 0, 0
        best_len, best_l = float("inf"), 0

        for r in range(len(s)):
            window[s[r]] = window.get(s[r], 0) + 1
            if (s[r] in tMap and window[s[r]] == tMap[s[r]]): # this checks if for the distinct character whether the number of it matches as well
                formed += 1

            while formed == required: # valid → try to shrink
                if r - l + 1 < best_len:
                    best_len = r - l + 1
                    best_l = l
                    
                window[s[l]] -= 1
                if s[l] in tMap and window[s[l]] < tMap[s[l]]:
                    formed -= 1  # s[l] just stopped being satisfied
                l += 1
        return "" if best_len == float("inf") else s[best_l:best_l + best_len]


            

            
             
