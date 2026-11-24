class Solution {
    public int longestConsecutive(int[] nums) {
        // use hashset to track nums for each num
        // we treat it as start of sequence 
        // and find if the next num is in map
        // time: O(N)
        // space: O(1)
        HashSet<Integer> track = new HashSet<>();
        for(int n:nums){
            track.add(n);
        }

        int longest = 0;
        for (int n: track){
            if (!track.contains(n-1)){ // we are at the start of a sequence
                int length = 1;
                while(track.contains(n + length)){
                    length++;
                }
                longest = Math.max(longest, length);
            }
        }
        return longest;
    }
}
