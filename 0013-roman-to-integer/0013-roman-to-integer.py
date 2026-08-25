class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        alphabet={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        res=0
        for i in range(len(s)-1):
            if s[i]=='I' or s[i]=='X' or s[i]=='C':
                if alphabet[s[i]]<alphabet[s[i+1]]:
                    res-=alphabet[s[i]]
                    continue
            res+=alphabet[s[i]]
        res+=alphabet[s[-1]]
        return res 
        