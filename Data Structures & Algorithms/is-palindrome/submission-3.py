class Solution:
    def isPalindrome(self, s: str) -> bool:
        if s is None or not s:
            return False

        # sol 1
        # use stack -- slightly more complicated
        # time: O(N)
        # space: O(N)
        # stack = []
        # for c in s:
        #     if c.isalnum():
        #         stack.append(c.lower())
        
        # mid = len(stack)//2
        # for c in stack[:mid]:
        #     popped = stack.pop()
        #     if popped != c:
        #         return False
        
        # return True

        # sol 2
        # just use a string
        # time: O(N)
        # space: O(N)
        # newStr = ''
        # for c in s:
        #     if c.isalnum():
        #         newStr += c.lower()
        
        # return newStr == newStr[::-1]

        # sol 3
        # use 2 pointers
        # time: O(N)
        # space: O(1)

        i, j = 0, len(s)-1

        while i<j:
            # loop till we get alphabet or number
            while i<j and not s[i].isalnum():
                i += 1
            # loop till we get alphabet or number
            while i<j and not s[j].isalnum():
                j -= 1

            if s[i].lower() != s[j].lower():
                return False
            
            i += 1
            j -= 1

        return True 
        