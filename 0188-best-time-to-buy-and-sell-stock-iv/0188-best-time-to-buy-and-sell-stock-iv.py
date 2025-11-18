class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0 for _ in range(k+1)] for _ in range(2)]
        for i in range(n-1,-1,-1):
            temp = [[0 for _ in range(k+1)] for _ in range(2)]
            for buy in range(2):
                for cap in range(1,k+1):
                    if buy == 1:
                        temp[buy][cap] = max(-prices[i] + dp[0][cap], 0 + dp[1][cap])
                    else:
                        temp[buy][cap] = max(prices[i] + dp[1][cap-1], 0 + dp[0][cap])
            dp = temp
        return dp[1][k]