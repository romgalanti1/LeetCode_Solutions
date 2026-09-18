class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        n=len(asteroids)
        if n==0:
            return []
        stack=[asteroids[0]]
        for i in range(1,n):
            curr=asteroids[i]
            if curr<0:
                while stack and stack[-1]>0 and stack[-1]<abs(curr):
                    stack.pop()
                if stack and stack[-1]>0 and stack[-1]==abs(curr):
                    stack.pop()
                    continue
                if not stack or stack[-1]<0:
                    stack.append(curr)
            else:
                stack.append(curr)
        return stack
                    
