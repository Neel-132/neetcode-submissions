class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        buy = prices[0]
        for i in range(1, len(prices)):
            if prices[i] < buy:
                buy = prices[i]
            else:
                profit = prices[i] - buy
                if profit > max_profit:
                    max_profit = profit
        return max_profit