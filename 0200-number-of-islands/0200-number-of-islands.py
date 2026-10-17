class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        n = len(grid)
        m = len(grid[0])
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        visited = set()
        islands = 0

        def dfs(i,j):

            if (i,j) in visited:
                return
            if i >= n or i < 0 or j < 0 or j >= m:
                return
            if grid[i][j] == "0":
                return
            visited.add((i,j))
            
            for di,dj in directions:
                ni,nj = i + di,j + dj
                dfs(ni,nj)
            return

        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1" and (i,j) not in visited:
                    islands += 1
                    dfs(i,j)
        return islands
