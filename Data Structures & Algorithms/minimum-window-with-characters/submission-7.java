class Solution {
    public String minWindow(String s, String t) {
        if (t.isEmpty()) return "";

        HashMap<Character, Integer> freq = new HashMap<>();

        for(char c:t.toCharArray()){
            freq.put(c, freq.getOrDefault(c, 0) + 1);
        }

        int l=0;
        int match = freq.size(); // distinct chars to be satisfied
        int resLen = Integer.MAX_VALUE;
        int start = 0;

        for(int r = 0; r < s.length(); r++){
            char rc = s.charAt(r);
            if (freq.containsKey(rc)){
                freq.put(rc, freq.get(rc) - 1);
                if (freq.get(rc) == 0){
                    match--;
                }
            }

            while (match == 0){ // window is valid, shrink it
                if (r - l + 1 < resLen){
                    resLen = r - l + 1;
                    start = l;
                }

                char lc = s.charAt(l);
                if (freq.containsKey(lc)){ // could be duplicate and we can potentially shrink still
                    freq.put(lc, freq.get(lc) + 1);
                    if (freq.get(lc) == 1) match++; // we went from staisfied to unsatisfied
                }
                l++;
            }
        }
        return resLen == Integer.MAX_VALUE ? "":s.substring(start, start+resLen);
    }
}
