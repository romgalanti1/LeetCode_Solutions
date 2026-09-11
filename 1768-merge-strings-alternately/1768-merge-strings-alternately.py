class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        i=0
        j=0
        n=len(word1)
        m=len(word2)
        string1=list(word1)
        string2=list(word2)
        res=[]
        while i<n and j<m:
            res.append(string1[i])
            res.append(string2[j])
            i+=1
            j+=1
        if i<n:
            for x in range(i,n):
                res.append(string1[x])
        else:
            for x in range(j,m):
                res.append(string2[x])
        res="".join(res)
        return res