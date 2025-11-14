class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        dp = [0 for _ in range(amount+1)]
        for i in range(n):
            temp = [0 for _ in range(amount+1)]
            for j in range(amount+1):
                if i == 0:
                    if j%coins[i] == 0:
                        temp[j] = int(j/coins[i])
                    else:
                        temp[j] = sys.maxsize
                    continue
                not_take = dp[j]
                take = sys.maxsize
                if coins[i]<=j:
                    take = 1 + temp[j-coins[i]]
                temp[j] = min(take,not_take)
            dp = temp
        return dp[amount] if dp[amount] != sys.maxsize else -1