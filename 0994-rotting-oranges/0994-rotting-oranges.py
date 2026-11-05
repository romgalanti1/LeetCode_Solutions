class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # scan for rotting oranges to be the start nodes, append them to queue
        # bfs from them while keeping steps
        # scan at the end to see if there are any oranges left

        m = len(grid)
        n = len(grid[0])
        Q = deque()
        steps = 0

        # check for starting rotten oranges
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    Q.append((i, j, steps))
        
        dirs = [(0,1),(0,-1),(1,0),(-1,0)]

        # bfs using Q
        while Q:
            i, j, steps = Q.popleft()

            for di, dj in dirs: # check neighbors
                ni, nj = i + di, j + dj
                if ni < m and ni >= 0 and nj < n and nj >= 0 and grid[ni][nj] == 1:
                    grid[ni][nj] = 2
                    Q.append((ni, nj, steps + 1))
        
        # scan again to check if there are still fresh oranges

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    return -1

        return steps