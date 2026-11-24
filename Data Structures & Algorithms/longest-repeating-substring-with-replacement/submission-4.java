class Solution {
    public int characterReplacement(String s, int k) {
        // track freq of each character as we loop
        // variable to track the highest freq at any point
        // string - freq > k, we pop left 
        // time: O(N)
        // space: O(N)

        int l=0;
        int maxFreq = 0;
        int res = 0;
        HashMap<Character, Integer> freq = new HashMap<>();

        for(int r=0; r < s.length(); r++){
            char c = s.charAt(r);
            freq.put(c, freq.getOrDefault(c, 0)+1);

            maxFreq = Math.max(maxFreq, freq.get(c));

            while ((r-l+1) - maxFreq > k){
                freq.put(s.charAt(l), freq.get(s.charAt(l))-1);
                l ++;
            }

            res = Math.max(res, r - l + 1);
        }
        return res;

    }
}
