class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        # brute force, check every node as a root, and bfs the edges to find the height O(n^2)
        # roots with degree of one no need to check as root, 
        # so maybe check only roots with highest degree as roots first
        # so for sure need to check degrees and operate on highest degrees first
        # check bottom up, find the leaves first and trim them until 2 roots remain with indegree at most 1

        if n <= 2:
            return [i for i in range(n)]
        # build graph
        graph = defaultdict(set)
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)
        # initialize Q and remaining_leaves
        leaves = deque([i for i in range(n) if len(graph[i]) == 1]) #  append leaves into q
        remaining_leaves = n

        while remaining_leaves > 2:
            leaves_count = len(leaves)
            remaining_leaves -= leaves_count

            for _ in range(leaves_count):
                curr = leaves.popleft()                
                neighbor = graph[curr].pop()
                graph[neighbor].remove(curr)
                if len(graph[neighbor]) == 1:
                    leaves.append(neighbor)


        return list(leaves)

