class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if prices is None or not prices or len(prices) < 2:
            return 0

        # sol 1 - brute force 2 loops
        # time: O(N^2)
        # space: O(1)

        # max_profit = 0
        # for i in range(len(prices)):
        #     for j in range(i+1, len(prices)):
        #         max_profit = max(max_profit, prices[j] - prices[i])

        # return max_profit

        # sol 2 - sliding window/two pointers
        # time: O(N)
        # space: O(1)
        # use l r pointer, if l > r, update l to be r

        l, r = 0, 1
        max_profit = 0

        while l < r and r < len(prices):
            max_profit = max(max_profit, prices[r] - prices[l])
            if prices[l] > prices[r]:
                l = r
            r += 1
        
        return max_profit
            