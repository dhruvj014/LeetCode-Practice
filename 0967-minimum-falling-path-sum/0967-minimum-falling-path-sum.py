class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        if n == 0:
            return 0
        if n == 1:
            return matrix[0][0]
        dp = [-1 for _ in range(n)]
        mini = sys.maxsize
        for i in range(n):
            temp = [0 for _ in range(n)]
            for j in range(n):
                if i == 0:
                    temp[j] = matrix[i][j]
                    continue
                diag_left = dp[j-1] if j-1>=0 else sys.maxsize
                diag_right = dp[j+1] if j+1<n else sys.maxsize
                up = dp[j]
                temp[j] = min(up,min(diag_left,diag_right)) + matrix[i][j]
                if i == n-1:
                    mini = min(mini, temp[j])
            dp = temp
        return mini