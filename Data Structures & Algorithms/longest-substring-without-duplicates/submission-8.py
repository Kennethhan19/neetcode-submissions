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
        # res = 0
        # l = 0
        # seen = set()

        # for r in range(len(s)):
        #     while s[r] in seen:
        #         seen.remove(s[l])
        #         l += 1
        #     seen.add(s[r])
        #     res = max(res, len(seen))
        
        # return res

        #sol 3 - optimised sliding window
        # time: O(N)
        # space: O(N)

        l = 0
        seen = {}
        res = 0

        for r in range(len(s)):
            if s[r] in seen:
                l = max(seen[s[r]] + 1, l)
            seen[s[r]] = r
            res = max(res, r - l + 1)
        
        return res
