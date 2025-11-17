class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m = len(s)
        n = len(t)
        dp = [0 for _ in range(n+1)]
        for i in range(m+1):
            for j in range(n,-1,-1):
                if j == 0:
                    dp[j] = 1
                    continue
                if s[i-1] == t[j-1]:
                    dp[j] = dp[j-1] + dp[j]
        return dp[n]