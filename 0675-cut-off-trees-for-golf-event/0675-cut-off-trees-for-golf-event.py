class Solution(object):
    def cutOffTree(self, forest):
        """
        :type forest: List[List[int]]
        :rtype: int
        """
        # bfs to find shortest path between two nodes
        
        dirs = [(0,1),(0,-1),(1,0),(-1,0)]
        m = len(forest)
        n = len(forest[0])
        visited = set()
        heights = []
        for i in range(m):
            for j in range(n):
                if forest[i][j] > 1:
                    heights.append((forest[i][j],i,j))
        heights.sort(key = lambda x:x[0]) # find shortest path inbetween all two trees
        
        
        def bfs(sr, sc, tr, tc):
            if sr == tr and sc == tc:
                return 0
            visited = set()
            visited.add((sr,sc))
            q = deque([(sr, sc,0)])
            while q:
                cr, cc, steps = q.popleft()
                if (cr,cc) == (tr,tc):
                    return steps
                for dr, dc in dirs:
                    nr, nc = cr + dr, cc + dc
                    if 0 <= nr < m and 0 <= nc < n and (nr,nc) not in visited and forest[nr][nc] != 0:
                        q.append((nr,nc,steps + 1))
                        visited.add((nr,nc))
            return -1
        d = 0
        curr_r,curr_c = 0, 0
        
        for _,tr, tc in heights:
            steps = bfs(curr_r, curr_c, tr, tc)
            if steps == -1:
                return -1
        
            d += steps
            curr_r, curr_c = tr, tc
        return d
            