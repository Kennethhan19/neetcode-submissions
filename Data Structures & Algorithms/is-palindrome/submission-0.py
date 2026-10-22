class Solution:
    def isPalindrome(self, s: str) -> bool:
        if s is None or not s:
            return False

        stack = []
        for c in s:
            if c.isalpha() or c.isdigit():
                stack.append(c.lower())
        
        mid = len(stack)//2
        for c in stack[:mid]:
            popped = stack.pop()
            if popped != c:
                return False
        
        return True