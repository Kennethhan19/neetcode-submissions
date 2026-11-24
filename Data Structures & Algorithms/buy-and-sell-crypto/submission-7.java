class Solution {
    public int maxProfit(int[] prices) {
        // time O(N)
        // space O(1)
        int l = 0;
        int profit = 0;
        for (int r = 0; r < prices.length; r++){
            if(prices[l] > prices[r]){
                l=r;
            }
            
            profit = Math.max(profit, prices[r] - prices[l]);
        }
        return profit;
    }
}
