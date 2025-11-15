class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n, m = len(text1), len(text2)
        dp = [0] * (m + 1)

        for i in range(1, n + 1):
            temp = [0] * (m + 1)
            for j in range(1, m + 1):
                if text1[i - 1] == text2[j - 1]:
                    temp[j] = 1 + dp[j - 1]
                else:
                    temp[j] = max(dp[j], temp[j - 1])
            dp = temp 
        return dp[m]
    def minDistance(self, word1: str, word2: str) -> int:
        lcp = self.longestCommonSubsequence(word1, word2)
        return len(word1) + len(word2) - 2*lcp