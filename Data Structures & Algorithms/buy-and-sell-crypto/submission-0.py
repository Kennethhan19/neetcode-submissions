class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if prices is None or not prices:
            return 0
            
        # sol 1 - brute force 2 loops
        # time: O(N^2)
        # space: O(1)

        max_profit = 0
        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                max_profit = max(max_profit, prices[j] - prices[i])

        return max_profit