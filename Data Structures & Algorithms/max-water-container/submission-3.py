class Solution:
    def maxArea(self, heights: List[int]) -> int:
        if heights is None or not heights:
            return 0
        

        # time: O(N^2)
        # space: O(1)
        # max_water = 0
        # for i in range(len(heights)):
        #     for j in range(i+1, len(heights), 1):
        #         cur_water = min(heights[i], heights[j])*(j-i)
        #         max_water = max(max_water, cur_water)

        # return max_water

        # time: O(N)
        # space: O(1)
        max_water = 0
        l, r = 0, len(heights) - 1

        while l < r:
            cur_water = min(heights[l], heights[r])* (r - l)
            max_water = max(max_water, cur_water)
            if heights[l] == heights[r]:
                r -= 1
                l += 1
            elif heights[l] > heights[r]:
                r -= 1
            elif heights[l] < heights[r]:
                l += 1
        
        return max_water
