class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        m = len(grid[0])
        dp = [0] * m
        dp[0] = grid[0][0]
        for c in range(1,m):
            dp[c] = dp[c-1] + grid[0][c]
        
        for r in range(1,n):
            dp[0] += grid[r][0]
            for c in range(1,m):
                dp[c] = grid[r][c] + min(dp[c-1],dp[c])
        
        return dp[-1]