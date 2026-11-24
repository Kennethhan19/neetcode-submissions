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
        String size = "";
        while(str.charAt(i) != '#'){
            size = size + str.charAt(i);
            i++;
        }

        i++;
        int j = i + Integer.parseInt(size);
        res.add(str.substring(i, j));
        i = j;
       }
       return res;
    }
}
