class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # sol 1
        # map of key: sorted str | value: [str1, str2]
        # time: O(m*nlogn) m - num of str, n longest str
        # space: O(m*n)
        # grp = {}
        # for s in strs:
        #     sorted_s = tuple(sorted(s))
        #     if sorted_s in grp:
        #         grp[sorted_s].append(s)
        #     else:
        #         grp[sorted_s] = [s]
        
        # return list(grp.values())

        #sol 2

        if strs is None or not strs:
            return []
        
        grp = {}
        for s in strs:
            cnt = self.countFreq(s)
            if cnt in grp:
                grp[cnt].append(s)
            else:
                grp[cnt] = [s]

        return list(grp.values())    

    def countFreq(self, s):
        cnt = [0]*26
        for c in s:
            cnt [ord(c) - ord('a')] += 1
        return tuple(cnt)


