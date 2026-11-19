class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # time: O(N)
        # space: O(N)
        # stack holds indices of days that haven't found a warmer day yet;
        # their temps are non-increasing from bottom to top.
        # for each day, pop every day on the stack that's colder than today —
        # today is their answer, so res[j] = i - j. then push today.
        # anything left on the stack at the end never got a warmer day → stays 0.
        if len(temperatures) == 1:
            return [0]

        stack = []
        res = [0]*len(temperatures)

        for i, t in enumerate(temperatures):
            while stack and t > temperatures[stack[-1]]:
                j = stack.pop()
                res[j] = i - j
            stack.append(i)
        
        return res
                
            