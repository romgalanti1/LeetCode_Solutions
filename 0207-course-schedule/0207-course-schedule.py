class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        graph = defaultdict(list)
        for after,before in prerequisites:
            graph[before].append(after)
        visited = set()
        visiting = set()

        def dfs(node):
            if node in visiting:
                return False
            if node in visited:
                return True
            visiting.add(node)
            for neighbor in graph[node]:
                if not dfs(neighbor):
                    return False
            visiting.remove(node)
            visited.add(node)
            return True
        
        for course in range(numCourses):
            if course not in visited:
                if not dfs(course):
                    return False
        return True
            
        
        
        

            
        