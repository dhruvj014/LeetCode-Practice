class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [0 for _ in range(amount + 1)]
        for i in range(n):
            temp = [0 for _ in range(amount + 1)]
            for j in range(amount+1):
                if i == 0:
                    if j == 0 or j%coins[i] == 0:
                        temp[j] = 1
                        continue
                not_pick = dp[j] 
                pick = temp[j - coins[i]] if coins[i] <= j else 0
                temp[j] = pick + not_pick
            dp = temp
        return dp[amount]                