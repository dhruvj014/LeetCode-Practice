class Solution:
    def isPalindrome(self, s: str) -> bool:
        return s==s[::-1]
    def minCut(self, s: str) -> int:
        n = len(s)
        if self.isPalindrome(s):
            return 0
        dp = [0 for _ in range(n+1)]
        for i in range(n-1,-1,-1):
            mincost = sys.maxsize
            for j in range(i,n):
                if self.isPalindrome(s[i:j+1]):
                    cost = 1 + dp[j+1]
                    mincost = min(mincost,cost)
            dp[i] = mincost
        return dp[0] - 1