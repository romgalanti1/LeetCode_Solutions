class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        cntr1 = Counter(s)
        cntr2 = Counter(t)
        return cntr1 == cntr2
        