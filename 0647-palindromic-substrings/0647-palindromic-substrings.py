class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        count = 0
        def expand(left,right):
            c = 0
            while left >= 0 and right < n and s[left] == s[right]:
                left -= 1
                right += 1
                c += 1
            return c
        for i in range(n):
            count += expand(i,i)
            count += expand(i,i+1)
        return count