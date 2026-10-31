class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s is None or not s:
            return 0

        # brute force
        # time: O(N^2)
        # space: O(N)
        # res = 0
        # for i in range(len(s)):
        #     dup = set()
        #     dup.add(s[i])
        #     for j in range(i+1, len(s), 1):
        #         if s[j] in dup:
        #             break
        #         dup.add(s[j])
        #     res = max(res, len(dup))
        # return res

        # sol 2 - sliding window
        # Time: O(N)
        # Space: O(N)
        res = 0
        l = 0
        dup = set()

        for r in range(len(s)):
            while s[r] in dup:
                dup.remove(s[l])
                l += 1
            dup.add(s[r])
            res = max(res, len(dup))
        
        return res