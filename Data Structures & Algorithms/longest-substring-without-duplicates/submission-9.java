class Solution {
    public int lengthOfLongestSubstring(String s) {
        // sliding window - use l r pointers, expand right first
        // when encounter duplicate we start popping left
        // every new addition to string we re compute longest
        // time: O(n)
        // space: O(N)
        
        int longest = 0;
        int l = 0;
        Set<Character> substring = new HashSet<>();

        for(int r = 0; r<s.length(); r++){
            while(substring.contains(s.charAt(r))){
                substring.remove(s.charAt(l));
                l++;                
            }

            substring.add(s.charAt(r));
            longest = Math.max(longest, substring.size());
        }

        return longest;
    }
}
