class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        # dfs and search for cycles , if cycle found return []
        # else append to array all neighbors in dfs
        
        visited = set()
        visiting = set()
        output = []
        graph = defaultdict(list)
        
        for u, v in prerequisites:
            graph[v].append(u)
        
        def dfs(i):
            if i in visited:
                return True
            if i in visiting:
                return False
            visiting.add(i)
            for neighbor in graph[i]:
                if neighbor not in visited:
                    if not dfs(neighbor):
                        return False
            output.append(i)
            visiting.remove(i)
            visited.add(i)
            return True
        
        for i in range(numCourses):
            if i not in visited:
                if not dfs(i):
                    return []
        return output[::-1]