class Solution {
    // append number and then a hashtag and the the string

    public String encode(List<String> strs) {
        StringBuilder res = new StringBuilder();

        for (String s: strs){
            res.append(s.length()).append('#').append(s);
        }
        return res.toString();
    }

    public List<String> decode(String str) {
       int i = 0;
       List<String> res = new ArrayList<>();

       while(i < str.length()){
            int size = 0;
            while(str.charAt(i) != '#'){
                size = size * 10 + (str.charAt(i) - '0');
                i++;
            }

            i++; // skip #
            res.add(str.substring(i, i + size));
            i += size;
       }
       return res;
    }
}
