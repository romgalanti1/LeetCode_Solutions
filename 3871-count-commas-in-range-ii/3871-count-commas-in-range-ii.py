class Solution(object):
    def countCommas(self, n):
        """
        :type n: int
        :rtype: int
        """
        commas=1
        start=1000
        res=0
        while n>=start:
            res+= (n-start) + 1
            start=start * 1000
            commas+=1
        return res