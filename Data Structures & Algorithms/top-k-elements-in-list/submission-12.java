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
        
        // build the buckets
        for(Map.Entry<Integer, Integer> e: freq.entrySet()){
            int f = e.getValue();
            if (buckets[f] == null) buckets[f] = new ArrayList<>();
            buckets[f].add(e.getKey());
        }

        int[] res = new int[k];
        int index = 0;
        for(int i=buckets.length-1; i > -1 && index < k; i--){
            if (buckets[i] == null) continue;
            for(int n: buckets[i]){
                res[index++] = n;
                if(index == k){
                    return res;
                }
            }
        }
        
        return res;
    }
}
