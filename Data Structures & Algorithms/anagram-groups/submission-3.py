class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # sol 1
        # map of key: sorted str | value: [str1, str2]
        # time: O(n*mlogm) n - num of str, m longest str
        # space: O(n*m)
        # grp = {}
        # for s in strs:
        #     sorted_s = tuple(sorted(s))
        #     if sorted_s in grp:
        #         grp[sorted_s].append(s)
        #     else:
        #         grp[sorted_s] = [s]
        
        # return list(grp.values())

        #sol 2
        # instead of sorting, use array of 26 (26 chars)
        # get relative position from a by using ord(c) - ord('a')
        # then array index is the position and the number at index represents the count of that character
        # time: O(n*m)
        # space: O(n*m)
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


