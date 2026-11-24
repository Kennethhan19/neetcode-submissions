class Solution {
    public boolean isPalindrome(String s) {

        // two pointers
        // time: O(N)
        // space: O(N)
        // loop from start and end, skip when encounter non digit/letter
        // compare when we have two digit/letter
        int l = 0, r = s.length()-1;

        while (l < r){
            while(l < r && !Character.isDigit(s.charAt(l)) && !Character.isLetter(s.charAt(l))){
                l++;
            }

            while(l < r && !Character.isDigit(s.charAt(r)) && !Character.isLetter(s.charAt(r))){
                r--;
            }

            if(Character.toLowerCase(s.charAt(l)) != Character.toLowerCase(s.charAt(r))){
                return false;
            }

            l++;
            r--;
        }
        return true; 
    }
}
