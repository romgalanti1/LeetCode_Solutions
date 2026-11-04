class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        # search for cycle in directed graph -> if theres a cycle return False else return True
        # build the graph:
        # 1. build defaultdict
        # 2. iterate through prereqs
        # 3. prereq[1] -> prereq[0]
        
        # find a cycle:
        # 1.iterate in range numcourses
        # 2. dfs each node while keeping visiting set and visited set
        # at the start of dfs add to visiting set and at the end remove
        # if removed then add to visited set, means the connected component doesnt have a cycle
        # if you finish all nodes return True
        
        graph = defaultdict(list)
        for post, pre in prerequisites:
            graph[pre].append(post)
        
        visited = set()
        visiting = set()
        def dfs(i):
            if i in visiting:
                return False
            visiting.add(i)
            for neighbor in graph[i]:
                if neighbor not in visited:
                    if not dfs(neighbor):
                        return False
            visiting.remove(i)
            visited.add(i)
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True
            
                    
            
        
        
        

            
        