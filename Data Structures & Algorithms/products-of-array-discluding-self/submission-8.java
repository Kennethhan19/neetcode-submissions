class Solution {
    public int[] productExceptSelf(int[] nums) {
        // use pre and post
        // time: O(N)
        // space: O(1) or O(N) if counting output array
        int[] res = new int[nums.length]; 
        res[0] = 1;
        for(int i=1; i<nums.length; i++){
            res[i] = res[i-1]*nums[i-1]; 
        }

        // use variable to track product to the right at pos i
        int right = 1;
        for(int i=nums.length-1; i>=0; i--){
            res[i] *= right;
            right *= nums[i];
        }

        return res;
    }
}  
