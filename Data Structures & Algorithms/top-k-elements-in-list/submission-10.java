class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        // first build the freq map
        // then group based on freq 

        // Time: O(N)
        // Space: O(N)

        HashMap<Integer, Integer> freq = new HashMap<>();
        List<Integer>[] buckets = new List[nums.length + 1];

        // build freq map
        for(int n: nums){
            freq.putIfAbsent(n, 0);
            freq.put(n, freq.get(n)+1);
        }

        for (int i = 0; i<buckets.length; i++){
            buckets[i] = new ArrayList<>();
        }
        
        // build the buckets
        for(int n: freq.keySet()){
            buckets[freq.get(n)].add(n);
        }

        int[] res = new int[k];
        int index = 0;
        for(int i=buckets.length-1; i > -1 && index < k; i--){
            List<Integer> bucket = buckets[i];
            for(int n: bucket){
                res[index++] = n;
                if(index == k){
                    return res;
                }
            }
        }
        
        return res;
    }
}
