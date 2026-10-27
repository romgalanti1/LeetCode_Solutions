class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        # if digit add to k via k = k * 10 + int(char)
        # if [ call recursive encoding function
        # if ] return recursion
        
        n = len(s)
        
        def dfs(i):
            
            res = []
            k = 0
            while i < n:
                char = s[i]
                if char.isdigit():
                    k = k * 10 + int(s[i])
                    i += 1
                elif char == "[":
                    sub_str, next_index = dfs(i + 1)
                    res.append(sub_str * k)
                    k = 0
                    i = next_index
                elif char == "]":
                    return "".join(res), i + 1
                else:
                    res.append(char)
                    i += 1
            return "".join(res), i
        
        decoded, _ = dfs(0)
        return decoded