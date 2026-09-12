import math
class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        n=len(str1)
        m=len(str2)
        len_gcd=math.gcd(n,m)
        if str1+str2!=str2+str1:
            return ""
        else:
            return str1[:len_gcd]