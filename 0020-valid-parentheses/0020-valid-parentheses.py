class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        closed = {")": 0,"}" : 1,"]": 2}
        opn = {"(" : 0, "{" : 1, "[" : 2}
        stack = []
        for char in s:
            if char in opn:
                stack.append(char)
            else:
                if not stack:
                    return False
                else:
                    if opn[stack[-1]] != closed[char]:
                        return False
                    else:
                        stack.pop()
        return not stack
