class DSU:
    def __init__(self,n):
        self.parent = [i for i in range(n)]
        self.rank = [1] * n
        self.num_components = n
    
    def find(self,x):
        if self.parent[x] == x:
            return x
        
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self,x,y):
        root_x = self.find(x)
        root_y = self.find(y)
        
        if root_x != root_y:
            if self.rank[root_x] < self.rank[root_y]:
                root_x, root_y = root_y, root_x
            self.parent[root_y] = root_x
            
            if self.rank[root_x] == self.rank[root_y]:
                self.rank[root_x] += 1
                
            self.num_components += 1
            return True
        return False
    
class Solution(object):
    def removeStones(self, stones):
        """
        :type stones: List[List[int]]
        :rtype: int
        """
        total_stones = len(stones)
        dsu = DSU(20002)
        
        for r,c in stones:
            dsu.union(r,c + 10001)
            
        unique_roots = set(dsu.find(r) for r,c in stones)
        return total_stones - len(unique_roots)
        