class Solution(object):
    def crackSafe(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        start_node = "0" * (n - 1)
        visited = set()
        res = []
        
        def dfs(node):
            for x in range(k):
                edge = node + str(x)
                if edge not in visited:
                    next_node = edge[1:]
                    visited.add(edge)
                    dfs(next_node)
                    res.append(str(x))
        
        dfs(start_node)
        return start_node + "".join(res[::-1])
                    