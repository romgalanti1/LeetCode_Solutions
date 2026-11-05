# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        # binary search 
        lo = 1
        hi = n
        

        [1,2,3,4,5,6,7,8,9]
        while lo < hi:
            mid = (lo + hi) // 2
            if isBadVersion(mid): #first bad version can be mid or older
                hi = mid
            else:
                lo = mid + 1
        return lo
