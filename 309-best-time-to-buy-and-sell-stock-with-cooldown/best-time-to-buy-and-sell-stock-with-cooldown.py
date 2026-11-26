class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        n = len(prices)

        if n == 0:
            return 0
        hold = -prices[0]
        sold = 0
        rest = 0

        for i in range(1, n):
            prev_hold = hold
            prev_sold = sold
            prev_rest = rest

            hold = max(prev_hold, prev_rest - prices[i])
            sold = prev_hold + prices[i]
            rest = max(prev_rest, prev_sold)
        return max(sold, rest)  
            
        