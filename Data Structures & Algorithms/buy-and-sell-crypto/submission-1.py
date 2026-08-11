class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        for i in range(1, len(prices)):
            if prices[i] - min(prices[:i]) > max_profit:
                max_profit = prices[i] - min(prices[:i])
        return max_profit