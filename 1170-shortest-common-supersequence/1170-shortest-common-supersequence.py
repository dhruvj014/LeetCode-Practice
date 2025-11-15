class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        n = len(str1)
        m = len(str2)
        dp = [[-1 for _ in range(m+1)] for _ in range(n+1)]
        for i in range(n+1):
            for j in range(m+1):
                if i==0:
                    dp[0][j] = 0
                    continue
                if j==0:
                    dp[i][0] = 0
                    continue
                if str1[i-1] == str2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                    continue
                dp[i][j] = max(dp[i-1][j],dp[i][j-1])
        ctr = dp[len(str1)][len(str2)]
        if ctr == 0:
            return str1 + str2
        l = len(str1) + len(str2) - dp[len(str1)][len(str2)]
        sol = [""]*l
        i = n
        j = m
        l2 = l
        while i > 0 and j>0:
            if str1[i-1] == str2[j-1]:
                sol[l-1] = str1[i-1]
                l-=1
                i-=1
                j-=1
                continue
            elif dp[i-1][j] > dp[i][j-1]:
                sol[l-1] = str1[i-1]
                l-=1
                i-=1
                continue
            else:
                sol[l-1] = str2[j-1]
                l-=1
                j-=1
                continue
        while i>0:
            sol[l-1] = str1[i-1]
            l-=1
            i-=1
        while j>0:
            sol[l-1] = str2[j-1]
            l-=1
            j-=1
        return "".join(sol)
