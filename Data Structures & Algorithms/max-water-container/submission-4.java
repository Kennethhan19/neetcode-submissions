class Solution {
    public int maxArea(int[] heights) {
        // two pointers - shorter height is the limiting factor
        // move pointers based on which is shorter
        // if both same, move both pointers
        // time: O(N)
        // space: O(1)
        int l=0;
        int r = heights.length - 1;
        int water = 0;
        while (l < r){
            int limit = Math.min(heights[l], heights[r]);
            water = Math.max(water, limit*(r - l));

            if (heights[l] > heights[r]){
                r--;
            }else if(heights[l] < heights[r]){
                l++;
            }else{
                l++;
                r--;
            }
        }

        return water;
    }
}
