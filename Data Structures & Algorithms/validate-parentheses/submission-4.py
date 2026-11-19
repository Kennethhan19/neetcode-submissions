class Solution:
    def isValid(self, s: str) -> bool:
        # time: O(N)
        # space: O(1)
        pair = {
            ')':'(',
            '}':'{',
            ']':'['
        }

        if len(s) % 2 != 0:
            return False

        stack = []
        for c in s:
            if c in pair:
                if not stack or stack.pop() != pair[c]:
                    return False
            else:
                stack.append(c)
            
        return not stack