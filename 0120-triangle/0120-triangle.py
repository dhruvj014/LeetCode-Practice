class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if len(triangle) == 1:
            return triangle[0][0]
        n = len(triangle)
        dp = [-1 for _ in range(len(triangle[-1]))] 
        for i in range(n-1,-1,-1):
            temp = [-1 for _ in range(len(triangle[i]))]
            for j in range(len(triangle[i])-1,-1,-1):
                if i == n-1:
                    temp[j] = triangle[i][j]
                    continue
                mini = min(dp[j],dp[j+1])
                temp[j] = mini + triangle[i][j]
            dp = temp
        return dp[0]