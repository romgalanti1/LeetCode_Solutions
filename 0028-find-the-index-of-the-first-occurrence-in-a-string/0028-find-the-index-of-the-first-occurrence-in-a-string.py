class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        m = len(needle)
        n = len(haystack)
        
        for i in range(n-m+1):
            if haystack[i:i+m] == needle:
                return i
        return -1