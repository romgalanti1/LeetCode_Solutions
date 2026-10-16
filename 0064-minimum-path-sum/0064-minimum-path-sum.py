class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        m = len(grid[0])
        dp = [[grid[i][j] for j in range(m)] for i in range(n)]
        dp[0][0] = grid[0][0]
        for r in range(n):
            for c in range(m):
                if r == 0 and c == 0:
                    continue
                elif r == 0:
                    dp[r][c] += dp[r][c-1]
                elif c == 0:
                    dp[r][c] += dp[r-1][c]
                else:
                    dp[r][c] += + min(dp[r-1][c],dp[r][c-1])
        return dp[-1][-1]