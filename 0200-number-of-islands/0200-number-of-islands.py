class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])

        def dfs(i,j):
            if i >= m or j >= n or i < 0 or j < 0 or grid[i][j] != "1":
                return
            grid[i][j] = 0
            dfs(i+1,j)
            dfs(i-1,j)
            dfs(i,j+1)
            dfs(i,j-1)
            return

        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    dfs(i,j)
                    count += 1
        return count
                
            