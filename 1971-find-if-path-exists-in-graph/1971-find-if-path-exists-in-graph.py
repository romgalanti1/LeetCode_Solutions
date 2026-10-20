class Solution(object):
    def validPath(self, n, edges, source, destination):
        """
        :type n: int
        :type edges: List[List[int]]
        :type source: int
        :type destination: int
        :rtype: bool
        """
        graph = defaultdict(set)
        for u,v in edges:
            graph[u].add(v)
            graph[v].add(u)

        q = deque([source])
        visited = set([source])
        while q:
            curr = q.popleft()
            if curr == destination:
                return True
            for neighbor in graph[curr]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    q.append(neighbor)
        return False


