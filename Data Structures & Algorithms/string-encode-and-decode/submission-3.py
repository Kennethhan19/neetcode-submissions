class Solution:
    # idea: use word len and a separator
    # time: O(N)
    # space: O(N)
    def encode(self, strs: List[str]) -> str:
        if strs is None or not strs:
            return ""

        res = ""
        for s in strs:
            res += (str(len(s)) + "#" + s)
        return res

    def decode(self, s: str) -> List[str]:
        if s is None or not s:
            return []

        i = 0
        words = []
        while i < len(s):
            size = ""
            while s[i] != '#':
                size += s[i]
                i += 1
            
            i += 1
            j = i + int(size)
            words.append(s[i:j])
            i = j 
        
        return words

