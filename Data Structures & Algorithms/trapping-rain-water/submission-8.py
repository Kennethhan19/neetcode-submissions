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
        # n = len(height)
        # lMax, rMax = [0]*n, [0]*n
        # lMax[0] = height[0]
        # for i in range(1, n):
        #     lMax[i] = max(lMax[i-1], height[i])
        # rMax[-1] = height[-1]
        # for i in range(n-2, -1, -1):
        #     rMax[i] = max(rMax[i+1], height[i])

        # res = 0
        # for i in range(n):
        #     res += min(lMax[i], rMax[i]) - height[i]

        # return res

        # sol 3 - use 2 pointers to track lMax and rMax so far
        # time: O(N)
        # space: O(1)
        l, r = 0, len(height) - 1
        lMax = rMax = 0
        res = 0

        while l < r:
            # tallest wall is somewhere in the right
            # so we have to find the limiting wall on the left
            if height[l] < height[r]:
                # if lMax becomes height[l] or lMax == height[l]
                # it means we have no taller wall on the left
                # therefore water above l wall wont hold and will spill to the left
                lMax = max(lMax, height[l])
                # and when we do lMax height with the condition in the comment
                # lMax - height[l] is 0 
                res += lMax - height[l]
                l += 1
            else:
                rMax = max(rMax, height[r])
                res += rMax - height[r]
                r -= 1
        return res

        