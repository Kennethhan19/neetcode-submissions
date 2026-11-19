class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if s is None or k is None or not s:
            return 0

        # brute force: 
        # 2 loops
        # for each substrin:
        # - track characters' freq using map
        # - always track the max freq in the substring
        # then substring length - max freq is how many characters we need to replace at least
        # Time: O(N^2)
        # Space: O(26)
        #
        # res = 0
        # for i in range(len(s)):
        #     cnt = {}
        #     max_Freq = 0
        #     for j in range(i, len(s)):
        #         cnt[s[j]] = cnt.get(s[j], 0) + 1
        #         max_Freq = max(max_Freq, cnt[s[j]])
        #         if ((j - i + 1) - max_Freq) <= k:
        #             res = max(res, (j-i+1))
        #         else:
        #             break
        # return res

        # sliding window 
        # same as above but when we meet j - i + 1 - max freq > k: we start incrementing the left pointer

        res = 0
        l = 0
        max_Freq = 0
        cnt = {}
        for r in range(len(s)):
            cnt[s[r]] = cnt.get(s[r], 0) + 1
            max_Freq = max(max_Freq, cnt[s[r]])

            while (r - l + 1 - max_Freq) > k:
                cnt[s[l]] -= 1
                l += 1
    
            res = max(res, r-l+1)
                
        return res


                
