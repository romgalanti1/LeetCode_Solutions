class Solution(object):
    def updateMatrix(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        # go through matrix, each one check its surronding neighbors
        # if 0 is a neighbor keep it at 1
        # if no neighbor is 0 then the distance is the minimum of all the neighbors + 1

        res = mat[:] 
        n = len(mat)
        m = len(mat[0])
        dirs = [(0,1),(0,-1),(1,0),(-1,0)]
        visited = set()
        Q = deque()

        def inbound(nr,nc):
            return nr < n and nr >= 0 and nc < m and nc >= 0

        for r in range(n):
            for c in range(m):
                if res[r][c] == 0:
                    Q.append((r,c,0))
                    visited.add((r,c))
        
        while Q:
            row, col, steps = Q.popleft()
            for dr, dc in dirs:
                nr, nc = row + dr, col + dc
                if inbound(nr,nc) and (nr,nc) not in visited:
                    Q.append((nr,nc,steps + 1))
                    res[nr][nc] = steps + 1
                    visited.add((nr,nc))
        return res