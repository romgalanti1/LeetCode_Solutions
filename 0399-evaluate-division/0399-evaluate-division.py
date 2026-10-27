class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        # a/b = 3 means a = 3b, b/c = 2 means b = 2c. to evaluate a/c, find a path from a -> c
        # ex. a = 3b, b = 2c , a=3*2c -> a = 6c , a/c = 6
        # if there is no path from x -> y return -1.0
        # build the graph: graph[a] = (3,b) means a = 3b (3,b) in graph[a] then (1/3,a) in graph[b]
        
        n = len(equations)
        graph = defaultdict(list)
        output = []
        
        for i in range(n): # build graph
            u, v = equations[i]
            graph[u].append((values[i], v))
            graph[v].append((1 / values[i], u))
        
        def bfs(start,finish):
            visited = set([start])
            q = deque([(start,1)])
            while q:
                curr, curr_val = q.popleft()
                if curr == finish:
                    return curr_val
                for value, neighbor in graph[curr]:
                    if neighbor not in visited:
                        q.append((neighbor, curr_val * value))
                        visited.add(neighbor)
            return -1.0
        
        output = []
        for u,v in queries:
            if u not in graph or v not in graph:
                output.append(-1.0)
            else:
                output.append(bfs(u,v))
        return output
                
            