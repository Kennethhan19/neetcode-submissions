class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s is None or not s:
            return 0
        
        # brute force: 
        # Time: O(N*M) - n len of string, m number of unique characters in string 
        # Space: O(m)

        # res = 0
        # for i in range(len(s)):
        #     duplicate = set()
        #     duplicate.add(s[i])
        #     longest = 1
        #     for j in range(i + 1, len(s), 1):
        #         if s[j] not in duplicate:
        #             duplicate.add(s[j])
        #             longest += 1
        #         else:
        #             break
            
        #     res = max(res, longest)

        # return res

        # sliding window
        # Time: O(N)
        # Space: O(M)
        
        index = {}
        l = 0
        res = 0

        for r in range(len(s)):
            if s[r] in index:
                l = max(index[s[r]] + 1, l)
            index[s[r]] = r
            res = max(res, r - l + 1)
      
        
        return res

        