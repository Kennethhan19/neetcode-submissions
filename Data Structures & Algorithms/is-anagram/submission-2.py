class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Time: O(N)
        # Space: O(N)
        if s is None or t is None or not s or not t:
            return False

        if len(s) != len(t):
            return False

        s_map, t_map = {}, {}

        for i in range(len(s)):
            s_map[s[i]] = s_map.get(s[i], 0) + 1
            t_map[t[i]] = t_map.get(t[i], 0) + 1
        
        return s_map == t_map
        