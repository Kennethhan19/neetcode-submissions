class Solution:
    def trap(self, height: List[int]) -> int:
        if height is None or not height:
            return 0

        # sol 1 - 2 loops: for every n search max left and right 
        # time: O(N^2)
        # space: O(1)
        # n = len(height)
        # res = 0

        # for i in range(n):
        #     lMax = rMax = height[i]
        #     # search left segment
        #     for l in range(i):
        #         lMax = max(lMax, height[l])
        #     # search right segment:
        #     for r in range(i+1, n):
        #         rMax = max(rMax, height[r])
            
        #     # min of lMax or rMax is the limiting side
        #     res += min(lMax, rMax) - height[i]
        
        # return res

        # sol 2: use leftMax, rightMax arr to track what the l or r max is at given i
        # time: O(N)
        # space: O(1)
        n = len(height)
        lMax, rMax = [0]*n, [0]*n
        lMax[0] = height[0]
        for i in range(1, n):
            lMax[i] = max(lMax[i-1], height[i])
        rMax[-1] = height[-1]
        for i in range(n-2, -1, -1):
            rMax[i] = max(rMax[i+1], height[i])

        res = 0
        for i in range(n):
            res += min(lMax[i], rMax[i]) - height[i]

        return res


