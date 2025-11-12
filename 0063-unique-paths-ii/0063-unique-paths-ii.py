class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        if obstacleGrid[0][0] == 1 or obstacleGrid[m-1][n-1] == 1:
            return 0
        ctr = 0
        dp = [0]*n
        for j in range(n-1, -1, -1):
            if obstacleGrid[m-1][j] == 1:
                dp[j] = 0
            else:
                dp[j] = dp[j+1] if j+1 < n else 1
        for i in range(m-2,-1,-1):
            temp = [0]*n
            for j in range(n-1,-1,-1):
                if obstacleGrid[i][j] == 1:
                    temp[j] = 0
                else:
                    down = dp[j]
                    right = temp[j+1] if j+1 < n else 0
                    temp[j] = down + right
            dp = temp
        return dp[0]