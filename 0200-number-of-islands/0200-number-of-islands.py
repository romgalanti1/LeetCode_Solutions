class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        dirs = [(0,1),(0,-1),(1,0),(-1,0)]
        
        def dfs(i,j):
            if i >= m or i < 0 or j >= n or j  < 0:
                return
            if grid[i][j] == "0":
                return
            grid[i][j] = "0"
            for di, dj in dirs:
                ni, nj = i + di, j + dj
                dfs(ni,nj)
            return
        
        islands = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    dfs(i,j)
                    islands += 1
        return islands
                        
