class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        // time: O(N*S) - n is number of string and s is longest string
        // space: O(N*S)
        HashMap<String, List<String>> group = new HashMap<>();

        for(String s: strs){
            String key = anagramKey(s);

            group.putIfAbsent(key, new ArrayList<>());
            group.get(key).add(s);
        }

        return new ArrayList<>(group.values());
    }

    private String anagramKey(String s){
        int[] freq = new int[26];
        for(char c: s.toCharArray()){
            freq[c - 'a'] ++;
        }

        return Arrays.toString(freq);
    }
}
