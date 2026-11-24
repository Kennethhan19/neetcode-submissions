class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        // sort and then use two pointer for the second loop or to find the pair inside the main loop
        // time: O(NLogN) sort + O(N^2)\
        // space: O(N) for sorting
        Arrays.sort(nums);
        List<List<Integer>> res = new ArrayList<>();
        
        for (int i=0; i<nums.length; i++){
            if(nums[i]>0) break; // impossible to have triplets that add to 0 after sorting
            if(i>0 && nums[i] == nums[i-1]) continue; // skip duplicates

            int l = i+1, r = nums.length - 1;

            while(l<r){
                int sum = nums[i] + nums[l] + nums[r];
                if(sum == 0){
                    res.add(Arrays.asList(nums[i], nums[l], nums[r]));
                    l++;
                    r--;
                    while(l<r && nums[l] == nums[l - 1]){ // skip duplicates
                        l++;
                    }
                }else if(sum > 0){
                    r--;
                }else{
                    l++;
                }
            }
        }

        return res;
    }
}
