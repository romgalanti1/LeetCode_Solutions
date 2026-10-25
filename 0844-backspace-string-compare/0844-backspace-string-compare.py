class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        #use stack pop with # check if stacks are equal at the end O(n) time O(n) space
        def buildstack(string):
            stack = []
            for char in string:
                if stack and char == "#":
                    stack.pop()
                elif char != "#":
                    stack.append(char)
            return stack
        
        stacks = buildstack(s)
        stackt = buildstack(t)
        
        return stacks == stackt
        
        