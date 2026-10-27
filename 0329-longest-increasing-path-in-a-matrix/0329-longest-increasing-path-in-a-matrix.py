class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        m = len(matrix)
        n = len(matrix[0])
        memo = [[0] * n for _ in range(m)] # memo[r][c] = longest increasing sequence starting from r,c
        dirs = [(0,1),(0,-1),(1,0),(-1,0)]
        
        def dfs(i,j):
            if i >= m or i < 0 or j >= n or j < 0:
                return 0
            if memo[i][j] != 0:
                return memo[i][j]
            res = 1
            for di, dj in dirs:
                ni,nj = i + di, j + dj
                if ni < m and ni >= 0 and nj < n and nj >= 0 and matrix[i][j] < matrix[ni][nj]:
                    res = max(res,1 + dfs(ni,nj))
            memo[i][j] = res
            return memo[i][j]
        
        longest = float("-inf")
        for i in range(m):
            for j in range(n):
                longest = max(longest,dfs(i,j))
        return longest