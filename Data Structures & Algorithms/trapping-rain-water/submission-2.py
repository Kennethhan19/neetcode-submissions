class Solution:
    def trap(self, height: List[int]) -> int:
        if height is None or not height:
            return 0

        # sol 1: 2 loops
        # time: O(N^2)
        # space: O(1)
        # res = 0
        # for i in range(len(height)):
        #     lMax = rMax = height[i]
        #     for l in range(i):
        #         lMax = max(lMax, height[l])
        #     for r in range(i+1, len(height)):
        #         rMax = max(rMax, height[r])

        #     res += min(lMax, rMax) - height[i]
        
        # return res

        # sol 2: prefix and postfix 
        # time: O(N)
        # space: O(N)
        # n = len(height)
        # pre = [0]*n
        # post = [0]*n
        # pre[0] = height[0]
        # for i in range(1, n):
        #     pre[i] = max(height[i], pre[i-1])

        # post[n-1] = height[n-1]
        # for i in range(n - 2, -1, -1):
        #     post[i] = max(post[i+1], height[i])

        # res = 0
        # for i in range(n):
        #     res += min(pre[i], post[i]) - height[i]       

        # return res     

        # sol 3
        # time: O(N)
        # space: O(1)
        l, r = 0, len(height) - 1
        lMax, rMax = height[l], height[r]
        res = 0
        while l<r:
            if lMax <= rMax:
                l += 1
                lMax = max(lMax, height[l])
                res += lMax - height[l]    
            else:
                r -= 1
                rMax = max(rMax, height[r])
                res += rMax - height[r]
        return res