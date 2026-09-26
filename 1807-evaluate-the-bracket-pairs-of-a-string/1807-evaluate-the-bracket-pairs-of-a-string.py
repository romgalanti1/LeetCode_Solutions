class Solution(object):
    def evaluate(self, s, knowledge):
        """
        :type s: str
        :type knowledge: List[List[str]]
        :rtype: str
        """
        d = {}
        for key, value in knowledge:
            d[key] = value
        res = []
        i = 0
        n = len(s)
        while i < n:
            if s[i] == "(":
                i += 1
                key = []
                while s[i] != ")":
                    key.append(s[i])
                    i+= 1
                i += 1
                key = "".join(key)
                res.append(d.get(key,"?"))
            else:
                res.append(s[i])
                i += 1
        return "".join(res)