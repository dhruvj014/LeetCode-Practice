class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini = prices[0]
        profit = 0
        for price in prices:
            cost = price - mini
            mini = min(mini, price)
            profit = max(profit, cost)
        return profit