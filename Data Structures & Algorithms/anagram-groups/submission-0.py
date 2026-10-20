class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # sol 1
        # map of key: sorted str | value: [str1, str2]
        
        grp = {}
        for s in strs:
            sorted_s = tuple(sorted(s))
            if sorted_s in grp:
                grp[sorted_s].append(s)
            else:
                grp[sorted_s] = [s]
        
        return list(grp.values())
